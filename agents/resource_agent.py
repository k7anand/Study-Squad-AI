from dotenv import load_dotenv
import os

from google import genai

from mcp_servers.resource_server import get_learning_resources

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))



class ResourceAgent:
    

    def recommend_resources(self, topic: str):
        
        """Rule-based resource recommendations."""
        print("Resource Agent Activated!")
        resources = get_learning_resources(topic)
        return {"topic": topic, "resources": resources}


    def recommend_resources_ai(self, topic: str):
        
        """AI-powered resource recommendations."""
        print("AI Resource Agent Activated!")
        resources = get_learning_resources(topic)

        if "message" in resources[0]:
            return resources[0]["message"]

        resource_summary = "\n".join(f"- {resource['channel']}: {resource['title']}" for resource in resources)

        prompt = f"""
        You are an educational tutor. A student needs help with the topic: {topic}.
        The following YouTube learning resources are available:
        {resource_summary}.

        Please provide:
        1. A short explanation of why this topic is important.
        2. The recommended order to study these resources.
        3. A one-sentence explanation for each resource.
        4. A short motivational message.

        Keep the response concise and student-friendly.
        """
        
        response = client.models.generate_content(model = "gemini-3.5-flash", contents = prompt)
        return response.text
