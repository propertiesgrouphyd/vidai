from pathlib import Path

file = Path("data/categories.js")

text = file.read_text()

marker = "\n]);"

add = r'''

    {
        id: "cybersecurity",
        label: "Cybersecurity",
        purpose: "professional",
        description:
            "Security, privacy, protection, and cyber technologies."
    },

    {
        id: "cloud-computing",
        label: "Cloud Computing",
        purpose: "professional",
        description:
            "Cloud platforms, infrastructure, and services."
    },

    {
        id: "data-science",
        label: "Data Science",
        purpose: "professional",
        description:
            "Data analysis, analytics, and intelligent systems."
    },

    {
        id: "software-development",
        label: "Software Development",
        purpose: "professional",
        description:
            "Software engineering, applications, and development practices."
    },

    {
        id: "product-management",
        label: "Product Management",
        purpose: "professional",
        description:
            "Product strategy, planning, and user experience."
    },

    {
        id: "project-management",
        label: "Project Management",
        purpose: "professional",
        description:
            "Planning, execution, and delivery management."
    },

    {
        id: "science",
        label: "Science",
        purpose: "professional",
        description:
            "Scientific concepts, research, and discoveries."
    },

    {
        id: "real-estate",
        label: "Real Estate",
        purpose: "business",
        description:
            "Property, construction, and real estate business."
    },

    {
        id: "e-commerce",
        label: "E-Commerce",
        purpose: "business",
        description:
            "Online selling, marketplaces, and digital commerce."
    },

    {
        id: "growth",
        label: "Growth",
        purpose: "business",
        description:
            "Business expansion, acquisition, and scaling."
    },

    {
        id: "market-research",
        label: "Market Research",
        purpose: "business",
        description:
            "Customer insights, trends, and market analysis."
    },

    {
        id: "writing",
        label: "Writing",
        purpose: "creator",
        description:
            "Creative writing, publishing, and storytelling."
    },

    {
        id: "video-creation",
        label: "Video Creation",
        purpose: "creator",
        description:
            "Video content, scripts, and creator workflows."
    },

    {
        id: "podcast",
        label: "Podcast",
        purpose: "creator",
        description:
            "Podcast planning, scripts, and discussions."
    },

    {
        id: "training",
        label: "Training",
        purpose: "education",
        description:
            "Courses, workshops, and professional training."
    }
'''

if marker not in text:
    raise SystemExit("Marker not found")

text = text.replace(marker, "," + add + "\n]);", 1)

file.write_text(text)

print("✓ Categories expanded")
