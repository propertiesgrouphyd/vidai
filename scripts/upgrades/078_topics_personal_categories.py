from pathlib import Path

FILE = Path("data/topics.js")

text = FILE.read_text(encoding="utf-8")

marker = "\n\n\n]);"
if marker not in text:
    raise SystemExit("Closing marker not found.")

items = r'''

    /* =========================
       Personal Development
       ========================= */

    {
        id: "goal-setting",
        label: "Goal Setting",
        category: "personal-development",
        description:
            "Setting meaningful goals and creating action plans."
    },

    {
        id: "self-improvement",
        label: "Self Improvement",
        category: "personal-development",
        description:
            "Developing better habits, skills, and personal growth."
    },

    {
        id: "time-management",
        label: "Time Management",
        category: "personal-development",
        description:
            "Managing time effectively for work and life."
    },

    {
        id: "critical-thinking",
        label: "Critical Thinking",
        category: "personal-development",
        description:
            "Analyzing information and making better decisions."
    },

    {
        id: "problem-solving",
        label: "Problem Solving",
        category: "personal-development",
        description:
            "Finding practical and creative solutions."
    },

    {
        id: "confidence-building",
        label: "Confidence Building",
        category: "personal-development",
        description:
            "Developing self-confidence and self-belief."
    },

    {
        id: "motivation",
        label: "Motivation",
        category: "personal-development",
        description:
            "Building and maintaining personal motivation."
    },

    {
        id: "habit-building",
        label: "Habit Building",
        category: "personal-development",
        description:
            "Creating positive daily habits."
    },


    /* =========================
       Relationships
       ========================= */

    {
        id: "family-relationships",
        label: "Family Relationships",
        category: "relationships",
        description:
            "Building stronger family connections."
    },

    {
        id: "friendships",
        label: "Friendships",
        category: "relationships",
        description:
            "Creating and maintaining healthy friendships."
    },

    {
        id: "professional-relationships",
        label: "Professional Relationships",
        category: "relationships",
        description:
            "Building trust and collaboration at work."
    },

    {
        id: "communication-skills",
        label: "Communication Skills",
        category: "relationships",
        description:
            "Improving everyday communication."
    },

    {
        id: "conflict-management",
        label: "Conflict Management",
        category: "relationships",
        description:
            "Resolving disagreements respectfully."
    },

    {
        id: "teamwork",
        label: "Teamwork",
        category: "relationships",
        description:
            "Working effectively with others."
    },


    /* =========================
       Life Experience
       ========================= */

    {
        id: "life-lessons",
        label: "Life Lessons",
        category: "life-experience",
        description:
            "Experiences that teach valuable life lessons."
    },

    {
        id: "personal-stories",
        label: "Personal Stories",
        category: "life-experience",
        description:
            "Sharing meaningful personal experiences."
    },

    {
        id: "success-stories",
        label: "Success Stories",
        category: "life-experience",
        description:
            "Achievements, journeys, and milestones."
    },

    {
        id: "failure-lessons",
        label: "Failure Lessons",
        category: "life-experience",
        description:
            "Learning and growing from setbacks."
    },

    {
        id: "life-milestones",
        label: "Life Milestones",
        category: "life-experience",
        description:
            "Important moments and major achievements."
    },

    {
        id: "inspiration",
        label: "Inspiration",
        category: "life-experience",
        description:
            "Experiences that inspire positive action."
    }

'''

text = text.replace(marker, "," + items + marker, 1)

FILE.write_text(text, encoding="utf-8")

print("✓ Personal category topics added.")
