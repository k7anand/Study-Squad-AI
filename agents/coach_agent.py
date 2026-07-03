from dotenv import load_dotenv
import os

from google import genai

from mcp_servers.memory_server import get_weak_topics

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))



class CoachAgent:
    

    def analyze_progress(self):
        """Rule-based coaching."""
        
        weak_topics = get_weak_topics()

        if not weak_topics:
            return (
                "Great work! "
                "No weak topics have been identified."
            )

        recommendations = []
        

        for topic in weak_topics:

            recommendations.append(
                f"- {topic['subject']} | "
                f"{topic['topic']} "
                f"({topic['score']}%)"
            )


        return (
            "Areas that need improvement:\n\n"
            + "\n".join(recommendations)
        )


    def analyze_progress_ai(self):
        """AI-powered coaching using Gemini."""

        weak_topics = get_weak_topics()

        if not weak_topics:
            return (
                "Great work! "
                "No weak topics have been identified."
            )

        topic_summary = "\n".join(f"- {t['subject']} | {t['topic']} | {t['score']}%" for t in weak_topics)

        prompt = f"""
        You are an encouraging academic coach.

        The student currently has these weak topics:

        {topic_summary}.

        Please provide:

        1. A short performance summary.
        2. The topics that need improvement.
        3. Three specific study recommendations.
        4. A short motivational message.

        Keep the response concise and encouraging.

        If the student has no weak topics, then congratulate them on their progress.
        Suggest one way to keep practicing and encourage them to try on a more difficult level. 
        """
        
        try:
            response = client.models.generate_content(model = "gemini-3.5-flash", contents = prompt)
        except Exception as e:
            return(f"Unable to generate AI coaching advice!\n\n{e}")

        return response.text
        
            
