from pathlib import Path

FILE = Path("data/topics.js")

text = FILE.read_text(encoding="utf-8")

marker = "\n\n\n]);"
if marker not in text:
    raise SystemExit("Closing marker not found.")

items = r'''

    /* =========================
       Engineering
       ========================= */

    {
        id: "civil-engineering",
        label: "Civil Engineering",
        category: "engineering",
        description:
            "Infrastructure, buildings, roads, and public works."
    },

    {
        id: "mechanical-engineering",
        label: "Mechanical Engineering",
        category: "engineering",
        description:
            "Machines, manufacturing, and mechanical systems."
    },

    {
        id: "electrical-engineering",
        label: "Electrical Engineering",
        category: "engineering",
        description:
            "Electrical systems, power, and electronics."
    },

    {
        id: "electronics-engineering",
        label: "Electronics Engineering",
        category: "engineering",
        description:
            "Electronic circuits, embedded systems, and devices."
    },

    {
        id: "industrial-engineering",
        label: "Industrial Engineering",
        category: "engineering",
        description:
            "Process optimization and industrial productivity."
    },

    {
        id: "quality-engineering",
        label: "Quality Engineering",
        category: "engineering",
        description:
            "Engineering quality standards and continuous improvement."
    },


    /* =========================
       Sales
       ========================= */

    {
        id: "sales-strategy",
        label: "Sales Strategy",
        category: "sales",
        description:
            "Planning and executing successful sales strategies."
    },

    {
        id: "sales-negotiation",
        label: "Sales Negotiation",
        category: "sales",
        description:
            "Negotiating effectively with customers and partners."
    },

    {
        id: "sales-pipeline",
        label: "Sales Pipeline",
        category: "sales",
        description:
            "Managing leads from prospect to customer."
    },

    {
        id: "customer-retention",
        label: "Customer Retention",
        category: "sales",
        description:
            "Building long-term customer relationships."
    },

    {
        id: "b2b-sales",
        label: "B2B Sales",
        category: "sales",
        description:
            "Business-to-business sales practices."
    },

    {
        id: "b2c-sales",
        label: "B2C Sales",
        category: "sales",
        description:
            "Business-to-consumer sales strategies."
    },


    /* =========================
       Human Resources
       ========================= */

    {
        id: "recruitment",
        label: "Recruitment",
        category: "human-resources",
        description:
            "Hiring, sourcing, and recruiting talent."
    },

    {
        id: "employee-engagement",
        label: "Employee Engagement",
        category: "human-resources",
        description:
            "Improving employee satisfaction and participation."
    },

    {
        id: "performance-review",
        label: "Performance Review",
        category: "human-resources",
        description:
            "Evaluating employee performance and growth."
    },

    {
        id: "workplace-culture",
        label: "Workplace Culture",
        category: "human-resources",
        description:
            "Creating a healthy and productive work environment."
    },

    {
        id: "learning-development",
        label: "Learning & Development",
        category: "human-resources",
        description:
            "Employee training and career development."
    },

    {
        id: "employee-wellbeing",
        label: "Employee Wellbeing",
        category: "human-resources",
        description:
            "Supporting employee health and wellbeing."
    },


    /* =========================
       Design
       ========================= */

    {
        id: "graphic-design",
        label: "Graphic Design",
        category: "design",
        description:
            "Visual communication through graphics and layouts."
    },

    {
        id: "ui-design",
        label: "UI Design",
        category: "design",
        description:
            "Designing intuitive user interfaces."
    },

    {
        id: "ux-design",
        label: "UX Design",
        category: "design",
        description:
            "Creating effective user experiences."
    },

    {
        id: "design-systems",
        label: "Design Systems",
        category: "design",
        description:
            "Reusable components and design consistency."
    },

    {
        id: "branding-design",
        label: "Brand Identity Design",
        category: "design",
        description:
            "Creating logos, identity systems, and brand visuals."
    },

    {
        id: "typography",
        label: "Typography",
        category: "design",
        description:
            "Fonts, readability, and visual hierarchy."
    }
'''

text = text.replace(marker, "," + items + marker, 1)

FILE.write_text(text, encoding="utf-8")

print("✓ Engineering, Sales, HR and Design topics added.")
