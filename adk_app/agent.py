from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool
from adk_app.quiz_tool import quiz_generation_tool

quiz_tool = FunctionTool(quiz_generation_tool)

root_agent = Agent(
    model = "gemini-3.5-flash",
    name = "tutor_agent",
    description = "Study Squad AI Tutor Agent",
    instruction = """
    You are a study tutor. When a user requests a quiz, you must call quiz_generation_tool.
    Do not generate quiz questions yourself. Use the tool whenever possible.
    """,
    tools=[quiz_tool]
)
