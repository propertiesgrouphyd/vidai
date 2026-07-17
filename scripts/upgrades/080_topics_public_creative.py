from pathlib import Path

FILE = Path("data/topics.js")

text = FILE.read_text(encoding="utf-8")

marker = "\n\n\n]);"

if marker not in text:
    raise SystemExit("Closing marker not found.")

items = r'''

    /* =========================
       Government
       ========================= */

    {
        id: "government-administration",
        label: "Government Administration",
        category: "government",
        description:
            "Public administration, government systems, and services."
    },

    {
        id: "e-governance",
        label: "E-Governance",
        category: "government",
        description:
            "Digital government services and technology."
    },

    {
        id: "civic-services",
        label: "Civic Services",
        category: "government",
        description:
            "Public services and citizen support systems."
    },

    {
        id: "urban-development",
        label: "Urban Development",
        category: "government",
        description:
            "Cities, infrastructure, and urban planning."
    },


    /* =========================
       Public Policy
       ========================= */

    {
        id: "policy-development",
        label: "Policy Development",
        category: "public-policy",
        description:
            "Creating and evaluating public policies."
    },

    {
        id: "governance",
        label: "Governance",
        category: "public-policy",
        description:
            "Leadership, institutions, and governance systems."
    },

    {
        id: "social-policy",
        label: "Social Policy",
        category: "public-policy",
        description:
            "Policies affecting communities and society."
    },


    /* =========================
       Media
       ========================= */

    {
        id: "journalism",
        label: "Journalism",
        category: "media",
        description:
            "News reporting, investigation, and storytelling."
    },

    {
        id: "news-writing",
        label: "News Writing",
        category: "media",
        description:
            "Writing news articles and reports."
    },

    {
        id: "public-relations",
        label: "Public Relations",
        category: "media",
        description:
            "Managing public communication and reputation."
    },

    {
        id: "broadcasting",
        label: "Broadcasting",
        category: "media",
        description:
            "Radio, television, and digital broadcasting."
    },


    /* =========================
       Entertainment
       ========================= */

    {
        id: "movies",
        label: "Movies",
        category: "entertainment",
        description:
            "Film creation, reviews, and entertainment content."
    },

    {
        id: "television",
        label: "Television",
        category: "entertainment",
        description:
            "TV programs, shows, and media production."
    },

    {
        id: "theatre",
        label: "Theatre",
        category: "entertainment",
        description:
            "Stage performance and theatre arts."
    },

    {
        id: "dance",
        label: "Dance",
        category: "entertainment",
        description:
            "Dance, performance, and creative expression."
    },


    /* =========================
       Sports
       ========================= */

    {
        id: "cricket",
        label: "Cricket",
        category: "sports",
        description:
            "Cricket, players, teams, and analysis."
    },

    {
        id: "football",
        label: "Football",
        category: "sports",
        description:
            "Football, teams, tactics, and events."
    },

    {
        id: "basketball",
        label: "Basketball",
        category: "sports",
        description:
            "Basketball skills, teams, and competitions."
    },

    {
        id: "tennis",
        label: "Tennis",
        category: "sports",
        description:
            "Tennis players, techniques, and tournaments."
    },

    {
        id: "sports-management",
        label: "Sports Management",
        category: "sports",
        description:
            "Managing sports teams, events, and organizations."
    },


    /* =========================
       Music
       ========================= */

    {
        id: "music-creation",
        label: "Music Creation",
        category: "music",
        description:
            "Songwriting, composition, and music production."
    },

    {
        id: "music-production",
        label: "Music Production",
        category: "music",
        description:
            "Recording, mixing, and producing music."
    },

    {
        id: "music-performance",
        label: "Music Performance",
        category: "music",
        description:
            "Artists, performances, and live music."
    },

    {
        id: "music-business",
        label: "Music Business",
        category: "music",
        description:
            "Publishing, promotion, and music industry."
    }
'''

text = text.replace(marker, "," + items + marker, 1)

FILE.write_text(text, encoding="utf-8")

print("✓ Public and creative topics added.")
