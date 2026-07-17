from pathlib import Path

file = Path("data/topics.js")

text = file.read_text()

marker = "\n\n\n]);"

if marker not in text:
    raise SystemExit("Marker not found")

items = r'''

    /* =========================
       Leadership & Management
       ========================= */

    {
        id: "leadership",
        label: "Leadership",
        category: "leadership",
        description:
            "Leadership principles, responsibilities, and effective leadership."
    },

    {
        id: "decision-making",
        label: "Decision Making",
        category: "leadership",
        description:
            "Better decisions, critical thinking, and problem solving."
    },

    {
        id: "vision",
        label: "Vision",
        category: "leadership",
        description:
            "Creating vision, direction, and long-term goals."
    },

    {
        id: "strategy",
        label: "Strategy",
        category: "leadership",
        description:
            "Strategic thinking, planning, and execution."
    },

    {
        id: "team-building",
        label: "Team Building",
        category: "leadership",
        description:
            "Building effective teams and collaboration."
    },

    {
        id: "delegation",
        label: "Delegation",
        category: "leadership",
        description:
            "Assigning responsibilities and empowering people."
    },

    {
        id: "communication",
        label: "Communication",
        category: "leadership",
        description:
            "Effective communication and professional interaction."
    },

    {
        id: "conflict-resolution",
        label: "Conflict Resolution",
        category: "leadership",
        description:
            "Managing disagreements and finding solutions."
    },

    {
        id: "emotional-intelligence",
        label: "Emotional Intelligence",
        category: "leadership",
        description:
            "Understanding emotions and improving relationships."
    },

    {
        id: "trust-building",
        label: "Trust Building",
        category: "leadership",
        description:
            "Building trust, reliability, and strong relationships."
    },

    {
        id: "mentoring",
        label: "Mentoring",
        category: "leadership",
        description:
            "Guiding people through knowledge and experience."
    },

    {
        id: "coaching",
        label: "Coaching",
        category: "leadership",
        description:
            "Helping individuals improve performance and skills."
    },

    {
        id: "company-culture",
        label: "Company Culture",
        category: "leadership",
        description:
            "Building healthy workplace culture and values."
    },

    {
        id: "performance-management",
        label: "Performance Management",
        category: "leadership",
        description:
            "Goals, feedback, evaluation, and improvement."
    },

    {
        id: "change-management",
        label: "Change Management",
        category: "leadership",
        description:
            "Managing organizational change effectively."
    },

    {
        id: "innovation",
        label: "Innovation",
        category: "leadership",
        description:
            "Creating new ideas, improvements, and solutions."
    },

    {
        id: "negotiation",
        label: "Negotiation",
        category: "leadership",
        description:
            "Negotiation skills, agreements, and outcomes."
    },

    {
        id: "productivity",
        label: "Productivity",
        category: "leadership",
        description:
            "Improving focus, efficiency, and results."
    }
'''

text = text.replace(
    marker,
    "," + items + marker,
    1
)

file.write_text(text)

print("✓ Leadership topics added.")
