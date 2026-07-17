from pathlib import Path

file = Path("data/categories.js")

text = file.read_text()

marker = "\n]);"

if marker not in text:
    raise SystemExit("Closing marker not found")

items = r'''
    {
        id: "manufacturing",
        label: "Manufacturing",
        purpose: "professional",
        description:
            "Manufacturing systems, production, and industrial processes."
    },

    {
        id: "supply-chain",
        label: "Supply Chain",
        purpose: "professional",
        description:
            "Supply chain planning, logistics, and distribution."
    },

    {
        id: "logistics",
        label: "Logistics",
        purpose: "professional",
        description:
            "Transportation, delivery, and logistics management."
    },

    {
        id: "agriculture",
        label: "Agriculture",
        purpose: "professional",
        description:
            "Farming, agriculture technology, and rural development."
    },

    {
        id: "environment",
        label: "Environment",
        purpose: "professional",
        description:
            "Environment, sustainability, and climate topics."
    },

    {
        id: "energy",
        label: "Energy",
        purpose: "professional",
        description:
            "Energy systems, renewable energy, and power technologies."
    },

    {
        id: "government",
        label: "Government",
        purpose: "professional",
        description:
            "Government services, administration, and public communication."
    },

    {
        id: "public-policy",
        label: "Public Policy",
        purpose: "professional",
        description:
            "Policies, governance, and public affairs."
    },

    {
        id: "hospitality",
        label: "Hospitality",
        purpose: "professional",
        description:
            "Hotels, tourism services, and hospitality management."
    },

    {
        id: "travel",
        label: "Travel",
        purpose: "professional",
        description:
            "Travel experiences, tourism, and destinations."
    },

    {
        id: "food",
        label: "Food",
        purpose: "professional",
        description:
            "Food industry, recipes, and food communication."
    },

    {
        id: "fashion",
        label: "Fashion",
        purpose: "professional",
        description:
            "Fashion, design, and lifestyle industries."
    },

    {
        id: "retail",
        label: "Retail",
        purpose: "professional",
        description:
            "Retail business, stores, and customer experience."
    },

    {
        id: "media",
        label: "Media",
        purpose: "professional",
        description:
            "Media, journalism, and communication."
    },

    {
        id: "entertainment",
        label: "Entertainment",
        purpose: "professional",
        description:
            "Entertainment industry and creative communication."
    },

    {
        id: "sports",
        label: "Sports",
        purpose: "professional",
        description:
            "Sports, athletes, teams, and sports communication."
    },

    {
        id: "investment",
        label: "Investment",
        purpose: "business",
        description:
            "Investments, capital, and financial growth."
    },

    {
        id: "consulting",
        label: "Consulting",
        purpose: "business",
        description:
            "Advisory services, expertise, and consulting."
    },

    {
        id: "franchise",
        label: "Franchise",
        purpose: "business",
        description:
            "Franchise models, expansion, and operations."
    },

    {
        id: "international-business",
        label: "International Business",
        purpose: "business",
        description:
            "Global markets, trade, and international operations."
    },

    {
        id: "photography",
        label: "Photography",
        purpose: "creator",
        description:
            "Photography, visual storytelling, and creative work."
    },

    {
        id: "music",
        label: "Music",
        purpose: "creator",
        description:
            "Music creation, publishing, and performance."
    },

    {
        id: "design-creator",
        label: "Design Creator",
        purpose: "creator",
        description:
            "Creative design, visual content, and digital art."
    },

    {
        id: "community-creator",
        label: "Community Creator",
        purpose: "creator",
        description:
            "Community building and audience engagement."
    }
'''

text = text.replace(
    marker,
    "," + items + marker,
    1
)

file.write_text(text)

print("✓ Categories part 2 added.")
