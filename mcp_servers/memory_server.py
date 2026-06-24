from mcp.server.fastmcp import FastMCP

# Create MCP server:
mcp = FastMCP("Study Squad Memory Server")

# In-memory storage:
quiz_history: list[dict] = []



@mcp.tool()
def save_quiz_result(subject: str, topic: str, score: float) -> str:
    """Save a quiz result to memory."""
    quiz_history.append({"subject": subject, "topic": topic, "score": score})

    return (
        f"Saved result: "
        f"{subject} | {topic} | {score}%"
    )


@mcp.tool()
def get_quiz_history():
    """Retrieve all quiz results."""
    return quiz_history


@mcp.tool()
def get_weak_topics(threshold: float = 70):
    """Return topics with scores below threshold."""
    weak_topics = []

    for result in quiz_history:
        if result["score"] < threshold:
            weak_topics.append({"subject": result["subject"], "topic": result["topic"], "score": result["score"]})

    return weak_topics



if __name__ == "__main__":
    mcp.run()


