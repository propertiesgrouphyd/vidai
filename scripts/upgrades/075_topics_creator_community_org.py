from pathlib import Path

file = Path("data/topics.js")

text = file.read_text()

marker = "\n\n\n]);"

if marker not in text:
    raise SystemExit("Marker not found")

items = r'''

    /* =========================
       Creator
       ========================= */

    {
        id: "content-creation",
        label: "Content Creation",
        category: "content-creation",
        description:
            "Creating digital content for audiences and platforms."
    },

    {
        id: "storytelling",
        label: "Storytelling",
        category: "content-creation",
        description:
            "Stories, narratives, and emotional communication."
    },

    {
        id: "video-production",
        label: "Video Production",
        category: "video-creation",
        description:
            "Video planning, production, and publishing."
    },

    {
        id: "photography",
        label: "Photography",
        category: "photography",
        description:
            "Visual storytelling through photography."
    },

    {
        id: "podcasting",
        label: "Podcasting",
        category: "podcast",
        description:
            "Podcast planning, episodes, and discussions."
    },

    {
        id: "personal-brand",
        label: "Personal Brand",
        category: "personal-brand",
        description:
            "Building identity and reputation online."
    },

    {
        id: "audience-growth",
        label: "Audience Growth",
        category: "content-creation",
        description:
            "Growing audiences and improving engagement."
    },

    {
        id: "influencer-marketing",
        label: "Influencer Marketing",
        category: "content-creation",
        description:
            "Creator partnerships and digital influence."
    },

    {
        id: "creative-writing",
        label: "Creative Writing",
        category: "writing",
        description:
            "Creative stories, ideas, and written expression."
    },

    {
        id: "digital-art",
        label: "Digital Art",
        category: "design-creator",
        description:
            "Digital illustrations, visual design, and creativity."
    },


    /* =========================
       Community
       ========================= */

    {
        id: "social-impact",
        label: "Social Impact",
        category: "social-impact",
        description:
            "Positive social change and community development."
    },

    {
        id: "volunteer-work",
        label: "Volunteer Work",
        category: "social-impact",
        description:
            "Volunteering, service, and community contribution."
    },

    {
        id: "awareness-campaigns",
        label: "Awareness Campaigns",
        category: "social-impact",
        description:
            "Public awareness and information campaigns."
    },

    {
        id: "community-events",
        label: "Community Events",
        category: "events",
        description:
            "Planning and communicating community events."
    },

    {
        id: "public-communication",
        label: "Public Communication",
        category: "events",
        description:
            "Messages for public groups and communities."
    },

    {
        id: "nonprofit-activities",
        label: "Nonprofit Activities",
        category: "social-impact",
        description:
            "Nonprofit initiatives and organizational communication."
    },


    /* =========================
       Organization
       ========================= */

    {
        id: "internal-communication",
        label: "Internal Communication",
        category: "internal-communication",
        description:
            "Internal updates, announcements, and communication."
    },

    {
        id: "organization-policies",
        label: "Organization Policies",
        category: "institution",
        description:
            "Rules, guidelines, and organizational policies."
    },

    {
        id: "team-updates",
        label: "Team Updates",
        category: "internal-communication",
        description:
            "Team reports, updates, and progress communication."
    },

    {
        id: "reports",
        label: "Reports",
        category: "institution",
        description:
            "Business, project, and organizational reports."
    },

    {
        id: "documentation",
        label: "Documentation",
        category: "institution",
        description:
            "Process documents and organizational knowledge."
    },

    {
        id: "process-improvement",
        label: "Process Improvement",
        category: "operations",
        description:
            "Improving systems, workflows, and efficiency."
    },

    {
        id: "culture-building",
        label: "Culture Building",
        category: "institution",
        description:
            "Building values, teamwork, and organizational culture."
    }
'''

text = text.replace(
    marker,
    "," + items + marker,
    1
)

file.write_text(text)

print("✓ Creator, Community, Organization topics added.")
