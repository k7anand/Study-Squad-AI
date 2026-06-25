"""The coordinator agent decides who does what."""

from agents.tutor_agent import TutorAgent
from agents.coach_agent import CoachAgent
from agents.resource_agent import ResourceAgent
from mcp_servers.memory_server import save_quiz_result


class CoordinatorAgent:

    def __init__(self):
        self.tutor = TutorAgent()
        self.coach = CoachAgent()
        self.resource = ResourceAgent()

    def run_learning_session(self, subject, topic, difficulty):
        quiz = self.tutor.generate_assessment(subject, topic, difficulty)
        return {"subject": subject, "topic": topic, "difficulty": difficulty, "quiz": quiz}

    def complete_learning_session(self, subject, topic, score):
        save_quiz_result(subject, topic, score)
        coach_feedback = self.coach.analyze_progress_ai()
        resources = self.resource.recommend_resources_ai(topic)
        return {
            "subject": subject, "topic": topic, "score": score, "coach_feedback": coach_feedback, "recommended_resources": resources
        }

