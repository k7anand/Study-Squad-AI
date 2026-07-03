import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

st.set_page_config(
    page_title = "Study Squad AI",
    layout = "centered"
)

from agents.coordinator_agent import CoordinatorAgent
from mcp_servers.memory_server import reset_quiz_history

coordinator = CoordinatorAgent()
st.title("Study Squad AI")

st.write("""
    Welcome! Study Squad AI is your personalized AI learning assistant.

    Choose a subject, topic, and difficulty level to begin your study session!
""")


if st.button("Start New Learning Journey"):
    
    reset_quiz_history()

    if "session" in st.session_state:
        del st.session_state["session"]

    st.success("Previous learning history cleared!")


subject = st.selectbox("Subject", ["Math", "Science"])

topics = {
    "Math": ["Fractions", "Integers", "Decimals", "Measurement", "Trigonometry"],
    "Science": ["Forces", "Electricity", "Human Anatomy", "Organic Chemistry", "Darwin's Evolution"]
}

topic = st.selectbox("Topic", topics[subject])
difficulty = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])


if st.button("Generate Quiz"):
    with st.spinner("Generating quiz..."):
        st.session_state.session = coordinator.run_learning_session(subject, topic, difficulty)


if "session" in st.session_state:
    

    session = st.session_state.session
    st.success("Quiz generated successfully!")
    st.write(f"Subject: {session['subject']}")
    st.write(f"Topic: {session['topic']}")
    st.write(f"Difficulty: {session['difficulty']}")

    quiz = session["quiz"]
    student_answers = []
    

    for i, question in enumerate(quiz, start = 1):

        st.subheader(f"Question {i}")
        st.write(question["question"])

        answer = st.radio(
            f"Question {i}",
            options = list(question["options"].keys()),
            format_func = lambda x: f"{x}. {question['options'][x]}",
            key = f"question_{i}",
            label_visibility = "collapsed"
        )

        student_answers.append(answer)


    if st.button("Submit Quiz"):
        
        
        with st.spinner("Analyzing your quiz..."):
            results = coordinator.complete_learning_session(
                subject = session["subject"],
                topic = session["topic"],
                difficulty = session["difficulty"],
                quiz = quiz,
                student_answers = student_answers
            )

            grading = results["grading_results"]
            st.header("Quiz Results")
            st.metric("Score", f"{grading['score']}%")
            st.metric("Correct", f"{grading['correct']} / {grading['total']}")
        
        

        if grading["missed_questions"]:
            

            st.subheader("Questions to Review")
            

            for question in grading["missed_questions"]:

                st.write(
                    f"Question {question['question_number']}: "
                    f"{question['question']}"
                )

                st.write(f"Your answer: {question['student_answer']}")
                st.write(f"Correct answer: {question['correct_answer']}")
                st.divider()


        st.header("Coach Feedback")
        st.write(results["coach_feedback"])


        st.header("Recommended Resources")
        st.write(results["recommended_resources"]["summary"])

        for resource in results["recommended_resources"]["resources"]:
            st.markdown(f"### {resource['title']}")
            st.write(resource["channel"])
            st.link_button("Watch on YouTube", resource["video_url"])
