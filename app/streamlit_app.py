import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st # type: ignore
from agent_core.executor import run_executor
from agent_core.evaluator import run_evaluator
from agent_core.improver import run_improver
from agent_core.memory import Memory

st.title("Self-Evolving AI Agent")

memory = Memory()

task = st.text_area("Enter a task description:", value="Write a Python function to check palindromes.")

max_rounds = st.slider("Max Improvement Rounds:", 1, 5, 3)

if st.button("Run Agent Loop"):
    current_solution = run_executor(task)
    st.write(f"Initial Executor Output:\n{current_solution}")

    for round_num in range(1, max_rounds + 1):
        feedback = run_evaluator(current_solution)
        st.write(f"Round {round_num} Evaluator Feedback:\n{feedback}")

        improved = run_improver(current_solution, feedback)
        st.write(f"Round {round_num} Improved Solution:\n{improved}")

        memory.add_entry(round_num, current_solution, feedback, improved)
        current_solution = improved
