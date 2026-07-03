import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import streamlit as st
import pandas as pd
from agents.coordinator_agent import CoordinatorAgent
from mcp_servers.memory_server import reset_quiz_history
from database import get_all_quiz_results

st.set_page_config(page_title = "Quiz History", layout = "centered")
st.title("Quiz History")
st.write("View your previous quiz attempts stored in the SQLite database.")

if st.button("Reset Learning History"):
    reset_quiz_history()
    st.success("Learning history cleared.")
    st.rerun()

history = get_all_quiz_results()

if not history:

    st.info("No quiz history yet!")

else:

    df = pd.DataFrame(history)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Quizzes", len(df))

    with col2:
        st.metric("Average Score", f"{df['score'].mean():.1f}%")

    with col3:
        st.metric("Best Score", f"{df['score'].max():.1f}%")

    st.subheader("Score History")
    st.line_chart(df.set_index("id")["score"])

    st.subheader("Quiz History Table")
    st.dataframe(df, use_container_width = True)
