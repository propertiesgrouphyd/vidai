from pathlib import Path

file = Path("data/topics.js")

text = file.read_text()

marker = "\n\n\n]);"

if marker not in text:
    raise SystemExit("Marker not found")

items = r'''

    /* =========================
       Human & General Knowledge
       ========================= */

    {
        id: "finance",
        label: "Finance",
        category: "finance",
        description:
            "Money, financial concepts, and financial decision making."
    },

    {
        id: "accounting",
        label: "Accounting",
        category: "finance",
        description:
            "Accounting principles, records, and financial reporting."
    },

    {
        id: "personal-finance",
        label: "Personal Finance",
        category: "finance",
        description:
            "Saving, budgeting, investing, and money management."
    },

    {
        id: "economics",
        label: "Economics",
        category: "finance",
        description:
            "Markets, economies, and economic concepts."
    },

    {
        id: "history",
        label: "History",
        category: "general",
        description:
            "Historical events, people, and civilizations."
    },

    {
        id: "culture",
        label: "Culture",
        category: "general",
        description:
            "Cultures, traditions, and human societies."
    },

    {
        id: "philosophy",
        label: "Philosophy",
        category: "general",
        description:
            "Ideas, beliefs, ethics, and human thinking."
    },

    {
        id: "psychology",
        label: "Psychology",
        category: "general",
        description:
            "Human behavior, mind, and emotions."
    },

    {
        id: "lifestyle",
        label: "Lifestyle",
        category: "general",
        description:
            "Daily life, habits, and personal interests."
    },

    {
        id: "food-cooking",
        label: "Food & Cooking",
        category: "food",
        description:
            "Food, recipes, cooking, and culinary topics."
    },

    {
        id: "fitness",
        label: "Fitness",
        category: "healthcare",
        description:
            "Exercise, fitness, and healthy living."
    },

    {
        id: "parenting",
        label: "Parenting",
        category: "personal-development",
        description:
            "Parenting, family, and child development."
    },

    {
        id: "travel-experiences",
        label: "Travel Experiences",
        category: "travel",
        description:
            "Travel stories, destinations, and experiences."
    },

    {
        id: "climate-change",
        label: "Climate Change",
        category: "environment",
        description:
            "Climate, environmental challenges, and solutions."
    },

    {
        id: "spirituality",
        label: "Spirituality",
        category: "general",
        description:
            "Spiritual ideas, reflection, and personal meaning."
    }
'''

text = text.replace(
    marker,
    "," + items + marker,
    1
)

file.write_text(text)

print("✓ Human lifestyle topics added.")
