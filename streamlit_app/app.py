import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from agents.coordinator_agent import CoordinatorAgent
coordinator = CoordinatorAgent()

st.set_page_config(page_title = "Study Squad AI", layout = "centered")
st.title("Study Squad AI")

st.write("""
    Welcome! Study Squad AI is your personalized AI learning assistant.

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
    st.session_state.session = coordinator.run_learning_session(subject, topic, difficulty)


if "session" in st.session_state:
    

    session = st.session_state.session
    st.success("Quiz generated successfully!")
    st.write(f"Subject: {session['subject']}")
    st.write(f"Topic: {session['topic']}")
    st.write(f"Difficulty: {session['difficulty']}")

    quiz = session["quiz"]


    for i, question in enumerate(quiz, start = 1):

        st.subheader(f"Question {i}")
        st.write(question["question"])

        st.radio(
            f"Question {i}",
            options = list(question["options"].keys()),
            format_func = lambda x: f"{x}. {question['options'][x]}",
            key = f"question_{i}",
            label_visibility = "collapsed"
        )
