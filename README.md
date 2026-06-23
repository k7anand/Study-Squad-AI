# Study Squad AI

Study Squad AI is a multi-agent educational assistant designed to help students prepare for exams and strengthen their understanding of academic topics. Unlike traditional AI chatbots, Study Squad AI uses a team of specialized agents that collaborate to assess knowledge, identify weaknesses, recommend learning resources, and generate personalized learning plans. 

The project demonstrates modern agentic AI concepts that include:

- Google Agent Development Kit (ADK),
- Multi-agent orchestration,
- Model Context Protocol (MCP),
- Reusable Agent Skills, and
- Cloud deployment using Google Cloud Run.

## Repository Structure

agents/ - Specialized AI agents

mcp/ - MCP Servers and tool integrations

skills/ - Reusable agent skills

streamlit_app/ - User interface and application entry point

## Project Goals

The objectives for this project include:

- Building a multi-agent learning assistant using Google ADK,
- Implementing MCP Servers that provide external tools and memory,
- Developing reusable Agent Skills for educational workflows,
- Deploying the application publicly using Google Cloud Run, and
- Creating a competition-ready demonstration showing agent collaboration.

## System Architecture

The system contains a Coordinator Agent, three specialized agents, and two MCP servers.

**Coordinator Agent**:
Receives user requests and determines which agents should be activated.
Coordinates communication between agents and combines their outputs into a unified response.

**Tutor Agent**:
Generates quizzes and evaluates student responses.
Uses the Quiz Generation Skill to create topic-specific assessments.

**Coach Agent**:
Analyzes quiz performance and identifies knowledge gaps.
Uses information from the Memory MCP Server to provide personalized recommendations.

**Resource Agent**:
Searches for learning resources related to the student's topic of interest.
Uses the Resource MCP Server to retrieve educational content from external platforms.

**Resource MCP Server**:
Provides educational resource retrieval tools, including YouTube search and topic-specific learning recommendations.

**Memory MCP Server**:
Provides study session storage and retrieval tools, including quiz history, performance tracking, and identified knowledge gaps.

Agent Skills are reusable capabilities that can be shared across multiple agents. The initial implementation will include a quiz generation skill that can be used by both the Tutor Agent and Coach Agent.


## Technology Stack

- Python
- Google ADK
- MCP
- Gemini
- Streamlit
- SQLite
- Google Cloud Run

## Current Scope

The initial version of Study Squad AI focuses on:

- Three specialized agents (Tutor, Coach, Resource)
- One reusable Quiz Generation Skill
- Two MCP servers (Resource and Memory)
- Streamlit user interface
- Google Cloud Run deployment

Features such as calendar integration, adaptive learning, advanced analytics, and additional resource providers are considered future enhancements and are intentionally outside the scope of the initial release.
