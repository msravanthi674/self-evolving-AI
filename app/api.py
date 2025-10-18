from flask import Flask, request, jsonify
from flask_limiter import Limiter # type: ignore
from flask_limiter.util import get_remote_address # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import sqlite3
import os
from dotenv import load_dotenv # type: ignore

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Configure secret key from environment variable
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')

# Rate Limiting setup
limiter = Limiter(app, key_func=get_remote_address, default_limits=["100 per hour"])

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Database helper functions
def get_user(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    conn.close()
    return user

def add_user(username, password, email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
                  (username, generate_password_hash(password), email))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# Registration endpoint with rate limiting
@app.route('/api/auth/register', methods=['POST'])
@limiter.limit("10/minute")
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({"error": "Missing required fields"}), 400

    if get_user(username):
        return jsonify({"error": "Username already exists"}), 400

    if add_user(username, password, email):
        return jsonify({"message": "User registered successfully"}), 201
    else:
        return jsonify({"error": "Email must be unique"}), 400

# Login endpoint with JWT token generation and rate limiting
@app.route('/api/auth/login', methods=['POST'])
@limiter.limit("15/minute")
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = get_user(username)
    if not user or not check_password_hash(user[1], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({"token": token}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
