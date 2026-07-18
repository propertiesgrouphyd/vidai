"use strict";

/* ==========================================================================
   VIDHWAAN AI Writer
   Category Library
   Version : 3.0.0

   Categories are connected to Purpose.

   Flow:
   Purpose → Category → Topic
   ========================================================================== */


const VW_CATEGORIES = Object.freeze([


    /* =========================
       PERSONAL PURPOSE
       ========================= */


    {
        id: "personal-development",
        label: "Personal Development",
        purpose: "personal",
        description:
            "Self improvement, habits, discipline, confidence, and becoming better."
    },


    {
        id: "life-experiences",
        label: "Life Experiences",
        purpose: "personal",
        description:
            "Personal journeys, memories, experiences, and lessons from life."
    },


    {
        id: "mindset-growth",
        label: "Mindset & Growth",
        purpose: "personal",
        description:
            "Mental strength, positive thinking, resilience, and growth mindset."
    },


    {
        id: "health-wellness",
        label: "Health & Wellness",
        purpose: "personal",
        description:
            "Physical health, mental wellbeing, fitness, and healthy living."
    },


    {
        id: "productivity",
        label: "Productivity",
        purpose: "personal",
        description:
            "Time management, focus, routines, and improving daily efficiency."
    },


    {
        id: "relationships",
        label: "Relationships",
        purpose: "personal",
        description:
            "Family, friendships, communication, and human connections."
    },


    {
        id: "lifestyle",
        label: "Lifestyle",
        purpose: "personal",
        description:
            "Daily lifestyle choices, experiences, interests, and personal balance."
    },

    /* =========================
       PROFESSIONAL PURPOSE
       ========================= */


    {
        id: "technology",
        label: "Technology",
        purpose: "professional",
        description:
            "Technology trends, digital transformation, innovation, and emerging technologies."
    },


    {
        id: "engineering",
        label: "Engineering",
        purpose: "professional",
        description:
            "Engineering knowledge, projects, solutions, and technical advancements."
    },


    {
        id: "data-ai",
        label: "Data & Artificial Intelligence",
        purpose: "professional",
        description:
            "Artificial intelligence, machine learning, data science, and intelligent systems."
    },


    {
        id: "software-development",
        label: "Software Development",
        purpose: "professional",
        description:
            "Programming, software engineering, applications, and development practices."
    },


    {
        id: "cloud-cybersecurity",
        label: "Cloud & Cybersecurity",
        purpose: "professional",
        description:
            "Cloud infrastructure, security, privacy, and digital protection."
    },


    {
        id: "science-research",
        label: "Science & Research",
        purpose: "professional",
        description:
            "Scientific discoveries, research, experiments, and knowledge."
    },


    {
        id: "healthcare",
        label: "Healthcare",
        purpose: "professional",
        description:
            "Healthcare systems, medical innovation, and health technologies."
    },


    {
        id: "finance",
        label: "Finance",
        purpose: "professional",
        description:
            "Finance, accounting, economics, investments, and financial knowledge."
    },


    {
        id: "legal",
        label: "Legal",
        purpose: "professional",
        description:
            "Law, compliance, regulations, contracts, and legal expertise."
    },


    {
        id: "industry-insights",
        label: "Industry Insights",
        purpose: "professional",
        description:
            "Industry trends, market observations, and professional analysis."
    },

    /* =========================
       CAREER PURPOSE
       ========================= */


    {
        id: "job-search",
        label: "Job Search",
        purpose: "career",
        description:
            "Job opportunities, applications, resumes, and finding the right career opportunities."
    },


    {
        id: "career-growth",
        label: "Career Growth",
        purpose: "career",
        description:
            "Career advancement, promotions, professional progress, and long-term development."
    },


    {
        id: "skills-development",
        label: "Skills Development",
        purpose: "career",
        description:
            "Learning new skills, improving abilities, and becoming career-ready."
    },


    {
        id: "interview-preparation",
        label: "Interview Preparation",
        purpose: "career",
        description:
            "Interview techniques, preparation methods, and candidate guidance."
    },


    {
        id: "workplace-experience",
        label: "Workplace Experience",
        purpose: "career",
        description:
            "Employee experiences, office culture, workplace lessons, and professional life."
    },


    {
        id: "professional-branding",
        label: "Professional Branding",
        purpose: "career",
        description:
            "Building professional identity, reputation, and career visibility."
    },


    {
        id: "career-transitions",
        label: "Career Transitions",
        purpose: "career",
        description:
            "Changing careers, moving industries, and adapting to new opportunities."
    },

    /* =========================
       BUSINESS PURPOSE
       ========================= */


    {
        id: "business-strategy",
        label: "Business Strategy",
        purpose: "business",
        description:
            "Business planning, competitive strategy, market decisions, and growth direction."
    },


    {
        id: "sales",
        label: "Sales",
        purpose: "business",
        description:
            "Sales processes, customer acquisition, revenue generation, and sales performance."
    },


    {
        id: "customer-success",
        label: "Customer Success",
        purpose: "business",
        description:
            "Customer relationships, satisfaction, retention, and customer experience."
    },


    {
        id: "operations",
        label: "Operations",
        purpose: "business",
        description:
            "Business processes, efficiency, systems, and operational excellence."
    },


    {
        id: "product-management",
        label: "Product Management",
        purpose: "business",
        description:
            "Product planning, product decisions, user needs, and product improvement."
    },


    {
        id: "e-commerce",
        label: "E-Commerce",
        purpose: "business",
        description:
            "Online business, digital selling, marketplaces, and commerce strategies."
    },


    {
        id: "business-growth",
        label: "Business Growth",
        purpose: "business",
        description:
            "Scaling businesses, expansion strategies, and revenue growth."
    },


    {
        id: "partnerships",
        label: "Partnerships",
        purpose: "business",
        description:
            "Business collaborations, strategic partnerships, and alliances."
    },


    {
        id: "investment-finance",
        label: "Investment & Finance",
        purpose: "business",
        description:
            "Business finance, investments, funding decisions, and financial planning."
    }

 
]);


Object.freeze(VW_CATEGORIES);










