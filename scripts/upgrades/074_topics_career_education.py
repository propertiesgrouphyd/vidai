from pathlib import Path

file = Path("data/topics.js")

text = file.read_text()

marker = "\n\n\n]);"

if marker not in text:
    raise SystemExit("Marker not found")

items = r'''

    /* =========================
       Career
       ========================= */

    {
        id: "resume-building",
        label: "Resume Building",
        category: "job-search",
        description:
            "Creating effective resumes and career documents."
    },

    {
        id: "interview-preparation",
        label: "Interview Preparation",
        category: "interview",
        description:
            "Interview skills, answers, and preparation strategies."
    },

    {
        id: "career-planning",
        label: "Career Planning",
        category: "career-growth",
        description:
            "Career goals, pathways, and professional decisions."
    },

    {
        id: "skill-development",
        label: "Skill Development",
        category: "career-growth",
        description:
            "Learning skills and improving professional abilities."
    },

    {
        id: "professional-growth",
        label: "Professional Growth",
        category: "career-growth",
        description:
            "Improving expertise and career advancement."
    },

    {
        id: "personal-branding",
        label: "Personal Branding",
        category: "career-growth",
        description:
            "Building professional identity and reputation."
    },

    {
        id: "job-search",
        label: "Job Search",
        category: "job-search",
        description:
            "Finding opportunities and applying effectively."
    },

    {
        id: "workplace-communication",
        label: "Workplace Communication",
        category: "career-growth",
        description:
            "Professional communication at work."
    },

    {
        id: "networking",
        label: "Networking",
        category: "career-growth",
        description:
            "Building professional connections and relationships."
    },

    {
        id: "leadership-development",
        label: "Leadership Development",
        category: "career-growth",
        description:
            "Developing leadership capabilities."
    },


    /* =========================
       Education
       ========================= */

    {
        id: "learning-methods",
        label: "Learning Methods",
        category: "learning",
        description:
            "Effective learning techniques and approaches."
    },

    {
        id: "teaching-methods",
        label: "Teaching Methods",
        category: "teaching",
        description:
            "Teaching approaches and educational practices."
    },

    {
        id: "online-learning",
        label: "Online Learning",
        category: "learning",
        description:
            "Digital education and online learning systems."
    },

    {
        id: "research",
        label: "Research",
        category: "learning",
        description:
            "Research methods, analysis, and academic exploration."
    },

    {
        id: "study-techniques",
        label: "Study Techniques",
        category: "learning",
        description:
            "Study habits, memory, and exam preparation."
    },

    {
        id: "academic-writing",
        label: "Academic Writing",
        category: "learning",
        description:
            "Academic documents, papers, and formal writing."
    },

    {
        id: "science-education",
        label: "Science Education",
        category: "learning",
        description:
            "Science learning and explanation."
    },

    {
        id: "technology-education",
        label: "Technology Education",
        category: "learning",
        description:
            "Teaching technology concepts and digital skills."
    },

    {
        id: "language-learning",
        label: "Language Learning",
        category: "learning",
        description:
            "Language education and communication skills."
    },

    {
        id: "training-design",
        label: "Training Design",
        category: "training",
        description:
            "Creating courses, workshops, and training programs."
    }
'''

text = text.replace(
    marker,
    "," + items + marker,
    1
)

file.write_text(text)

print("✓ Career and Education topics added.")
