import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from agents.coordinator_agent import CoordinatorAgent

st.set_page_config(page_title = "Study Squad AI", layout = "centered")
st.title("Study Squad AI")

st.write("""
    Welcome!

    Study Squad AI is your personalized AI learning assistant.

    Choose a subject, topic, and difficulty level to begin your study session!
""")

subject = st.selectbox("Subject", ["Math", "Science"])

topics = {
    "Math": ["Fractions", "Integers", "Decimals", "Measurement", "Trigonometry"],
    "Science": ["Forces", "Electricity", "Human Anatomy", "Organic Chemistry", "Darwin's Evolution"]
}

topic = st.selectbox("Topic", topics[subject])
difficulty = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Quiz"):
    st.success("Milestone 12 Complete!")
    st.write(f"Subject: {subject}")
    st.write(f"Topic: {topic}")
    st.write(f"Difficulty: {difficulty}")
