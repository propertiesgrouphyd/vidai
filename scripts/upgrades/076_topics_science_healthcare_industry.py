from pathlib import Path

file = Path("data/topics.js")

text = file.read_text()

marker = "\n\n\n]);"

if marker not in text:
    raise SystemExit("Marker not found")

items = r'''

    /* =========================
       Science
       ========================= */

    {
        id: "physics",
        label: "Physics",
        category: "science",
        description:
            "Physics concepts, discoveries, and scientific explanations."
    },

    {
        id: "chemistry",
        label: "Chemistry",
        category: "science",
        description:
            "Chemical concepts, research, and applications."
    },

    {
        id: "biology",
        label: "Biology",
        category: "science",
        description:
            "Life sciences, organisms, and biological discoveries."
    },

    {
        id: "space-science",
        label: "Space Science",
        category: "science",
        description:
            "Space exploration, astronomy, and universe research."
    },

    {
        id: "research-methods",
        label: "Research Methods",
        category: "research",
        description:
            "Scientific research approaches and analysis."
    },

    {
        id: "scientific-discovery",
        label: "Scientific Discovery",
        category: "science",
        description:
            "New discoveries, inventions, and scientific progress."
    },


    /* =========================
       Healthcare
       ========================= */

    {
        id: "medicine",
        label: "Medicine",
        category: "healthcare",
        description:
            "Medical knowledge, healthcare practices, and treatments."
    },

    {
        id: "public-health",
        label: "Public Health",
        category: "healthcare",
        description:
            "Community health, prevention, and awareness."
    },

    {
        id: "wellness",
        label: "Wellness",
        category: "healthcare",
        description:
            "Health, lifestyle, and wellbeing."
    },

    {
        id: "healthcare-technology",
        label: "Healthcare Technology",
        category: "healthcare",
        description:
            "Digital health systems and medical technology."
    },

    {
        id: "medical-research",
        label: "Medical Research",
        category: "healthcare",
        description:
            "Healthcare studies and medical innovation."
    },


    /* =========================
       Legal
       ========================= */

    {
        id: "law",
        label: "Law",
        category: "legal",
        description:
            "Legal concepts, systems, and information."
    },

    {
        id: "contracts",
        label: "Contracts",
        category: "legal",
        description:
            "Contract writing, agreements, and terms."
    },

    {
        id: "compliance",
        label: "Compliance",
        category: "legal",
        description:
            "Rules, regulations, and compliance requirements."
    },

    {
        id: "intellectual-property",
        label: "Intellectual Property",
        category: "legal",
        description:
            "Patents, trademarks, copyrights, and ownership."
    },

    {
        id: "privacy",
        label: "Privacy",
        category: "legal",
        description:
            "Privacy laws, data protection, and security."
    },

    {
        id: "regulations",
        label: "Regulations",
        category: "legal",
        description:
            "Industry rules, standards, and regulations."
    },


    /* =========================
       Industry
       ========================= */

    {
        id: "construction",
        label: "Construction",
        category: "construction",
        description:
            "Construction projects, infrastructure, and development."
    },

    {
        id: "energy-industry",
        label: "Energy",
        category: "energy",
        description:
            "Energy production, renewable energy, and resources."
    },

    {
        id: "environmental-sustainability",
        label: "Environmental Sustainability",
        category: "environment",
        description:
            "Sustainability, conservation, and climate solutions."
    },

    {
        id: "agricultural-technology",
        label: "Agricultural Technology",
        category: "agriculture",
        description:
            "Modern farming, technology, and agriculture innovation."
    },

    {
        id: "transportation",
        label: "Transportation",
        category: "logistics",
        description:
            "Transport systems, mobility, and infrastructure."
    },

    {
        id: "supply-chain-management",
        label: "Supply Chain Management",
        category: "supply-chain",
        description:
            "Supply networks, inventory, and distribution."
    },

    {
        id: "hospitality-management",
        label: "Hospitality Management",
        category: "hospitality",
        description:
            "Hotels, tourism, and hospitality operations."
    },

    {
        id: "retail-business",
        label: "Retail Business",
        category: "retail",
        description:
            "Retail operations, customers, and commerce."
    },

    {
        id: "property-development",
        label: "Property Development",
        category: "real-estate",
        description:
            "Real estate projects, property, and development."
    }
'''

text = text.replace(
    marker,
    "," + items + marker,
    1
)

file.write_text(text)

print("✓ Science, Healthcare, Legal and Industry topics added.")
