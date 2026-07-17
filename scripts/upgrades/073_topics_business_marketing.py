from pathlib import Path

file = Path("data/topics.js")

text = file.read_text()

marker = "\n\n\n]);"

if marker not in text:
    raise SystemExit("Marker not found")

items = r'''

    /* =========================
       Business & Marketing
       ========================= */

    {
        id: "entrepreneurship",
        label: "Entrepreneurship",
        category: "business",
        description:
            "Starting businesses, entrepreneurial thinking, and innovation."
    },

    {
        id: "startup-building",
        label: "Startup Building",
        category: "business",
        description:
            "Startup creation, validation, and growth."
    },

    {
        id: "business-strategy",
        label: "Business Strategy",
        category: "business",
        description:
            "Strategic planning, decisions, and competitive advantage."
    },

    {
        id: "business-planning",
        label: "Business Planning",
        category: "business",
        description:
            "Business plans, goals, and execution planning."
    },

    {
        id: "business-models",
        label: "Business Models",
        category: "business",
        description:
            "Revenue models, value creation, and business structures."
    },

    {
        id: "revenue-growth",
        label: "Revenue Growth",
        category: "business",
        description:
            "Increasing revenue, expansion, and growth strategies."
    },

    {
        id: "customer-experience",
        label: "Customer Experience",
        category: "business",
        description:
            "Customer relationships, satisfaction, and loyalty."
    },

    {
        id: "sales-strategy",
        label: "Sales Strategy",
        category: "business",
        description:
            "Sales processes, techniques, and customer acquisition."
    },

    {
        id: "branding",
        label: "Branding",
        category: "business",
        description:
            "Brand identity, positioning, and reputation."
    },

    {
        id: "market-research",
        label: "Market Research",
        category: "business",
        description:
            "Markets, customers, trends, and insights."
    },

    {
        id: "competitive-analysis",
        label: "Competitive Analysis",
        category: "business",
        description:
            "Competitors, positioning, and market comparison."
    },

    {
        id: "investment",
        label: "Investment",
        category: "business",
        description:
            "Capital, investment decisions, and financial growth."
    },

    {
        id: "funding",
        label: "Funding",
        category: "business",
        description:
            "Fundraising, investors, and startup finance."
    },

    {
        id: "finance-management",
        label: "Finance Management",
        category: "business",
        description:
            "Business finance, budgeting, and financial planning."
    },

    {
        id: "business-operations",
        label: "Business Operations",
        category: "business",
        description:
            "Processes, efficiency, and operational excellence."
    },

    {
        id: "business-scaling",
        label: "Business Scaling",
        category: "business",
        description:
            "Growth systems, expansion, and scaling operations."
    },

    {
        id: "partnerships",
        label: "Partnerships",
        category: "business",
        description:
            "Business partnerships, collaborations, and alliances."
    },

    {
        id: "e-commerce",
        label: "E-Commerce",
        category: "business",
        description:
            "Online commerce, marketplaces, and digital selling."
    },


    {
        id: "digital-marketing",
        label: "Digital Marketing",
        category: "marketing",
        description:
            "Online marketing channels and strategies."
    },

    {
        id: "content-marketing",
        label: "Content Marketing",
        category: "marketing",
        description:
            "Content strategy, publishing, and audience growth."
    },

    {
        id: "social-media-marketing",
        label: "Social Media Marketing",
        category: "marketing",
        description:
            "Social platforms, engagement, and campaigns."
    },

    {
        id: "seo",
        label: "SEO",
        category: "marketing",
        description:
            "Search optimization and organic growth."
    },

    {
        id: "advertising",
        label: "Advertising",
        category: "marketing",
        description:
            "Advertising campaigns, messaging, and promotion."
    },

    {
        id: "brand-building",
        label: "Brand Building",
        category: "marketing",
        description:
            "Building strong brands and market presence."
    },

    {
        id: "email-marketing",
        label: "Email Marketing",
        category: "marketing",
        description:
            "Email campaigns, newsletters, and customer communication."
    },

    {
        id: "lead-generation",
        label: "Lead Generation",
        category: "marketing",
        description:
            "Finding prospects and creating business opportunities."
    },

    {
        id: "customer-acquisition",
        label: "Customer Acquisition",
        category: "marketing",
        description:
            "Attracting and converting new customers."
    },

    {
        id: "product-marketing",
        label: "Product Marketing",
        category: "marketing",
        description:
            "Product positioning, launches, and communication."
    },

    {
        id: "growth-marketing",
        label: "Growth Marketing",
        category: "marketing",
        description:
            "Experimentation, growth systems, and optimization."
    }
'''

text = text.replace(
    marker,
    "," + items + marker,
    1
)

file.write_text(text)

print("✓ Business and Marketing topics added.")
