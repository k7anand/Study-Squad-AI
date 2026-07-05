# Agent Skills

Agent Skills are reusable AI capabilities shared across multiple agents.

## Quiz Generation Skill

Generates multiple-choice questions using Gemini.



Inputs:



* subject,
* topic,
* difficulty,
* number of questions.



Outputs:



* question,
* answer choices,
* correct answer.



This skill is used by the Tutor Agent to generate personalized assessments and is also exposed as an ADK FunctionTool in the adk\_app demonstration.

