from mcp.server.fastmcp import FastMCP
from database import (
    initialize_database,
    insert_quiz_result,
    get_all_quiz_results,
    get_weak_topics as get_weak_topics_db,
    clear_database
)


# Create MCP server:
mcp = FastMCP("Study Squad Memory Server")

# Make sure that the database exists:
initialize_database()



@mcp.tool()
def save_quiz_result(subject: str, topic: str, score: float) -> str:
    """Save a quiz result to the database."""

    insert_quiz_result(subject, topic, score)

    return (
        f"Saved result: "
        f"{subject} | {topic} | {score}%"
    )


@mcp.tool()
def get_quiz_history():
    """Retrieve all quiz results."""
    return get_all_quiz_results()


@mcp.tool()
def get_weak_topics(threshold: float = 70):
    """Return topics with scores below the threshold."""
    return get_weak_topics_db(threshold)


@mcp.tool()
def reset_quiz_history():
    """Delete all stored quiz results."""
    clear_database()
    return "Quiz history has been cleared!"



if __name__ == "__main__":
    mcp.run()
    
