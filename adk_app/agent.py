from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash',
    name='tutor_agent',
    description='Study Squad AI Tutor Agent',
    instruction="""
    You are a study assistant that helps students learn.
    When asked to create a quiz, generate educational multiple-choice questions.
    """,
)