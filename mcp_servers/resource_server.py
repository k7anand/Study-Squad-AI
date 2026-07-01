from mcp.server.fastmcp import FastMCP

# Create MCP server:
mcp = FastMCP("Study Squad Resource Server")


# Resources:
resources = {
    
    "Fractions": [
        {
            "topic": "Fractions",
            "title": "Fractions Made EASY!",
            "channel": "TabletClass Math",
            "handle": "@tabletclass",
            "video_url": "https://www.youtube.com/watch?v=5hG8e9jGeaA",
            "difficulty": "Beginner"
        },
        {
            "topic": "Fractions",
            "title": "Everything to know about FRACTIONS in 30 minutes!",
            "channel": "JensenMath",
            "handle": "@MrJensenMath10",
            "video_url": "https://www.youtube.com/watch?v=8XmhGjgsiVc",
            "difficulty": "Beginner"
        },
        {
            "topic": "Fractions",
            "title": "Fraction Review | How to Add, Subtract, Multiply, and Divide Fractions",
            "channel": "Math with Mr. J",
            "handle": "@MathwithMrJ",
            "video_url": "https://www.youtube.com/watch?v=rl7e0djo9Go",
            "difficulty": "Intermediate"
        },
        {
            "topic": "Fractions",
            "title": "Adding Fractions with Unlike Denominators",
            "channel": "Math with Mr. J",
            "handle": "@MathwithMrJ",
            "video_url": "https://www.youtube.com/watch?v=CoCmsyFQ_Xc",
            "difficulty": "Intermediate"
        },
        {
            "topic": "Fractions",
            "title": "Simplifying Algebraic Fractions",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=WSQh4o3yu4I",
            "difficulty": "Advanced"
        }
    ],

    "Integers": [
        {
            "topic": "Integers",
            "title": "What's an Integer? | Integers Explained",
            "channel": "Math with Mr. J",
            "handle": "@MathwithMrJ",
            "video_url": "https://www.youtube.com/watch?v=OSfDRqxmXAE",
            "difficulty": "Beginner"
        },
        {
            "topic": "Integers",
            "title": "How to Add, Subtract, Multiply, and Divide Integers | A Review of Integers",
            "channel": "Math with Mr. J",
            "handle": "@MathwithMrJ",
            "video_url": "https://www.youtube.com/watch?v=O6bRgxVRoZ4",
            "difficulty": "Intermediate"
        },
        {
            "topic": "Integers",
            "title": "Order of Operations with Integers",
            "channel": "Math with Mr. J",
            "handle": "@MathwithMrJ",
            "video_url": "https://www.youtube.com/watch?v=03aAr9Fh2SQ",
            "difficulty": "Advanced"
        }
    ],

    "Decimals": [
        {
            "topic": "Decimals",
            "title": "Introduction to Decimals",
            "channel": "Khan Academy",
            "handle": "@khanacademy",
            "video_url": "https://www.youtube.com/watch?v=BItpeFXC4vA",
            "difficulty": "Beginner"
        },
        {
            "topic": "Decimals",
            "title": "Decimal Review | Add, Subtract, Multiply, and Divide Decimals",
            "channel": "Math with Mr. J",
            "handle": "@MathwithMrJ",
            "video_url": "https://www.youtube.com/watch?v=UCBXoLb2ItI",
            "difficulty": "Intermediate"
        },
        {
            "topic": "Decimals",
            "title": "Multiplying and Dividing by Powers of 10",
            "channel": "Math with Mr. J",
            "handle": "@MathwithMrJ",
            "video_url": "https://www.youtube.com/watch?v=HH-yrNS80Cg",
            "difficulty": "Advanced"
        }
    ],

    "Measurement": [
        {
            "topic": "Measurement",
            "title": "Metric Units of Length | Convert mm, cm, m and km",
            "channel": "Math with Mr. J",
            "handle": "@MathwithMrJ",
            "video_url": "https://www.youtube.com/watch?v=kOJFSH_Bn9U",
            "difficulty": "Beginner"
        },
        {
            "topic": "Measurement",
            "title": "Converting Units With Conversion Factors - Metric System Review & Dimensional Analysis",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=eK8gXP3pImU&t=26s",
            "difficulty": "Beginner"
        }
    ],

    "Trigonometry": [
        {
            "topic": "Trigonometry",
            "title": "Trigonometry For Beginners!",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=PUB0TaZ7bhA",
            "difficulty": "Beginner"
        },
        {
            "topic": "Trigonometry",
            "title": "Trig Identities",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=m1OitPmkydY",
            "difficulty": "Intermediate"
        },
        {
            "topic": "Trigonometry",
            "title": "Law of Cosines, Finding Angles & Sides, SSS & SAS Triangles",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=9CGY0s-uCUE",
            "difficulty": "Intermediate"
        }
    ],

    "Forces": [
        {
            "topic": "Forces",
            "title": "What Is a Force?",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=vZ0ehaOEZKE",
            "difficulty": "Beginner"
        },
        {
            "topic": "Forces",
            "title": "Newton's Law of Motion - First, Second & Third - Physics",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=g550H4e5FCY",
            "difficulty": "Intermediate"
        },
        {
            "topic": "Forces",
            "title": "Force Formulas - Static Friction, Kinetic Friction, Normal Force, Tension Force - Free Body Diagrams",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=wAygj3fIOcc",
            "difficulty": "Advanced"
        }
    ],

    "Electricity": [
        {
            "topic": "Electricity",
            "title": "Electricity - Basic Introduction",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=ybuhfEa-PrU",
            "difficulty": "Beginner"
        },
        {
            "topic": "Electricity",
            "title": "Coulomb's Law - Net Electric Force & Point Charges",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=kCp5yYjo9zE",
            "difficulty": "Intermediate"
        },
        {
            "topic": "Electricity",
            "title": "Electric Field Due To Point Charges - Physics Problems",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=V9RLc9EX1so",
            "difficulty": "Intermediate"
        }
    ],

    "Human Anatomy": [
        {
            "topic": "Human Anatomy",
            "title": "Introduction to Anatomy & Physiology: Crash Course Anatomy & Physiology #1",
            "channel": "CrashCourse",
            "handle": "@crashcourse",
            "video_url": "https://www.youtube.com/watch?v=uBGl2BujkPQ&t=154s",
            "difficulty": "Beginner"
        }
    ],

    "Organic Chemistry": [
        {
            "topic": "Organic Chemistry",
            "title": "Organic Chemistry - Basic Introduction",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=B_ketdzJtY8",
            "difficulty": "Beginner"
        },
        {
            "topic": "Organic Chemistry",
            "title": "Functional Groups",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=m9jM8lWxrAE",
            "difficulty": "Intermediate"
        },
        {
            "topic": "Organic Chemistry",
            "title": "IUPAC Nomenclature of Alkanes - Naming Organic Compounds",
            "channel": "The Organic Chemistry Tutor",
            "handle": "@TheOrganicChemistryTutor",
            "video_url": "https://www.youtube.com/watch?v=TYU_JluleME",
            "difficulty": "Advanced"
        }
    ],

    "Darwin's Evolution": [
        {
            "topic": "Darwin's Evolution",
            "title": "Darwin's theory of Evolution: A REALLY SIMPLE and Brief Explanation",
            "channel": "Science ABC",
            "handle": "@Scienceabc",
            "video_url": "https://www.youtube.com/watch?v=pybhlOhXkiM",
            "difficulty": "Beginner"
        },
        {
            "topic": "Darwin's Evolution",
            "title": "The Theory of Evolution (by Natural Selection)",
            "channel": "Cornerstones Education",
            "handle": "@cornerstones_edu",
            "video_url": "https://www.youtube.com/watch?v=BcpB_986wyk&t=18s",
            "difficulty": "Beginner"
        }
    ]
}



@mcp.tool()
def get_learning_resources(topic: str):
    """Retrieve learning resources for a given topic."""
    return resources.get(topic, [{"message": "No learning resources are available for this topic."}])


@mcp.tool()
def get_beginner_resources(topic: str):
    """Retrieve beginner learning resources for a topic."""

    topic_resources = resources.get(topic)

    if topic_resources is None:
        return [{"message": "Topic not found!"}]

    beginner_resources = [
        resource
        for resource in topic_resources
        if resource["difficulty"] == "Beginner"
    ]

    if beginner_resources:
        return beginner_resources

    return [{"message": "No beginner resources available!"}]


@mcp.tool()
def get_intermediate_resources(topic: str):
    "Retrieve intermediate learning resources for a topic."""

    topic_resources = resources.get(topic)

    if topic_resources is None:
        return [{"message": "Topic not found!"}]

    intermediate_resources = [
        resource
        for resource in topic_resources
        if resource["difficulty"] == "Intermediate"
    ]

    if intermediate_resources:
        return intermediate_resources

    return [{"message": "No intermediate resources available!"}]


@mcp.tool()
def get_advanced_resources(topic: str):
    """Retrieve advanced learning resources for a topic."""

    topic_resources = resources.get(topic)

    if topic_resources is None:
        return [{"message": "Topic not found!"}]

    advanced_resources = [
        resource
        for resource in topic_resources
        if resource["difficulty"] == "Advanced"
    ]

    if advanced_resources:
        return advanced_resources

    return [{"message": "No advanced resources available!"}]


if __name__ == "__main__":
    mcp.run()
