from dotenv import load_dotenv
import os

from google import genai

from mcp_servers.resource_server import get_learning_resources, get_beginner_resources, get_intermediate_resources, get_advanced_resources

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))



class ResourceAgent:


    def recommend_resources(self, topic: str):
        """Rule-based resource recommendations."""

        print("Resource agent has been activated!")
        resources = get_learning_resources(topic)
        return {"topic": topic, "resources": resources}


    def recommend_resources_ai(self, topic: str, difficulty: str):
        """AI-powered resource recommendations."""

        print("AI resource agent has been activated!")

        if difficulty == "Beginner":
            resources = get_beginner_resources(topic)
        elif difficulty == "Intermediate":
            resources = get_intermediate_resources(topic)
        elif difficulty == "Advanced":
            resources = get_advanced_resources(topic)
        else:
            resources = get_learning_resources(topic)

        if "message" in resources[0]:
            return {"summary": resources[0]["message"], "resources": []}

        resource_summary = "\n".join(f"- {resource['title']} ({resource['channel']})" for resource in resources)
        
        prompt = f"""
        You are an educational tutor.

        A student is studying:
        Topic: {topic}
        Difficulty: {difficulty}

        The following curated resources were retrieved from the Study Squad Resource MCP Server:

        {resource_summary}

        Please provide:
        1. Why this topic is important.
        2. The recommended order to study these resources.
        3. One sentence describing each resource.
        4. A short motivational message.

        Do not invent additional resources.
        Keep the response concise and student-friendly.
        """

        try:
            response = client.models.generate_content(model = "gemini-2.5-flash", contents = prompt)
        except Exception as e:
            return(f"Unable to generate AI content!\n\n{e}")

        return {"summary": response.text, "resources": resources}
