# 🚀 Self-Evolving AI Agent  
A multi-agent system that autonomously generates, evaluates, and improves solutions using Mistral AI’s powerful LLM in an iterative self-improvement loop.

[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)  [![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)   [![Mistral AI](https://img.shields.io/badge/Powered%20by-Mistral%20AI-8A2BE2?logo=openai&logoColor=white)](https://mistral.ai)   [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  

---

> ✨ *An innovative multi-agent system that learns, critiques, and improves itself — simulating how humans refine ideas through feedback loops.*

---

## 🧠 Overview

**Self-Evolving AI Agent** is a multi-agent architecture leveraging **Mistral AI’s cutting-edge LLM API** to autonomously:
- Generate solutions  
- Evaluate them critically  
- Iteratively improve upon them  

This closed-loop system mimics human creativity — producing progressively smarter and higher-quality outputs with minimal human input.

---

## ⚙️ Features

### 🤖 Multi-Agent Design
- **Executor Agent** — Crafts original solutions from user prompts.  
- **Evaluator Agent** — Analyzes and scores each result with detailed feedback.  
- **Improver Agent** — Refines and re-optimizes based on evaluator insights.  

### 🔄 Continuous Self-Improvement
- Agents communicate in feedback loops until the output reaches top quality.  

### 🧩 Tech Stack
- **Python**, **Streamlit**, and **Mistral AI SDK**  
- Modular architecture for easy scaling or custom agent addition  

---

## 🚀 Getting Started

### 🧾 Prerequisites
- Python **3.11+**
- Mistral API key → [Get one here](https://mistral.ai)
- Install dependencies:  
  ```bash
  pip install -r requirements.txt
  ```
### 💾 Installation
```bash
git clone https://github.com/msravanthi674/self-evolving-ai-agent.git
cd self-evolving-ai-agent
pip install -r requirements.txt
```

Create a .env file in the root directory:
```bash
MISTRAL_API_KEY=your_api_key_here
```

### 🖥️ Run Locally
```bash
streamlit run app/streamlit_app.py
```

### ☁️ Deployment

- Streamlit Cloud → one-click deploy by linking your GitHub repo.
- Supports secure API key management via environment variables.
- Optional: Deploy via Docker, Render, or Heroku for scalability.
---
### 🗂️ Project Structure
```bash
self-evolving-ai-agent/
├── agent_core/         # Core agent logic (executor, evaluator, improver)
├── app/                # Streamlit UI + orchestrator
├── .env                # Environment variables (not committed)
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```
---
### 🧩 Example Workflow

- User enters a task description.
- Executor Agent generates an initial solution.
- Evaluator Agent reviews and scores it.
- Improver Agent refines based on feedback.
- The cycle repeats — each iteration gets smarter.
---
### 💡 Future Enhancements
- 🧬 Reinforcement learning–based improvement scoring
- 🌐 Multi-model orchestration (OpenAI + Mistral hybrid)
- 🧠 Memory-based adaptive agent personalities
---
