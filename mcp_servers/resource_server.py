from mcp.server.fastmcp import FastMCP

# Create MCP server:
mcp = FastMCP("Study Squad Resource Server")


# Curated Resources:
resources = {
    
    "Fractions": [
        {"title": "Fractions", "channel": "Khan Academy"},
        {"title": "Fractions", "channel": "Math Antics"},
        {"title": "Fractions", "channel": "The Organic Chemistry Tutor"}
    ],

    "Integers": [
        {"title": "Integers", "channel": "Math Antics"},
        {"title": "Integers", "channel": "Khan Academy"}
    ],

    "Decimals": [
        {"title": "Decimals", "channel": "Khan Academy"},
        {"title": "Decimals", "channel": "Math Antics"}
    ],

    "Measurement": [
        {"title": "Measurement", "channel": "Khan Academy"}
    ],

    "Trigonometry": [
        {"title": "Trigonometry", "channel": "The Organic Chemistry Tutor"},
        {"title": "Trigonometry", "channel": "Khan Academy"}
    ],

    "Forces": [
        {"title": "Forces", "channel": "Crash Course"},
        {"title": "Forces", "channel": "Khan Academy"}
    ],

    "Electricity": [
        {"title": "Electricity", "channel": "Crash Course"},
        {"title": "Electricity", "channel": "Khan Academy"}
    ],

    "Human Anatomy": [
        {"title": "Human Anatomy", "channel": "Amoeba Sisters"},
        {"title": "Human Anatomy", "channel": "Crash Course"}
    ],

    "Organic Chemistry": [
        {"title": "Organic Chemistry", "channel": "The Organic Chemistry Tutor"}
    ],

    "Darwin's Evolution": [
        {"title": "Evolution", "channel": "Amoeba Sisters"},
        {"title": "Evolution", "channel": "Crash Course"}
    ]
}



@mcp.tool()
def get_learning_resources(topic: str):
    """Retrieve learning resources for a given topic."""
    return resources.get(topic, [{"message": "No learning resources are available for this topic."}])


if __name__ == "__main__":
    mcp.run()
