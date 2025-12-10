"""
Pre-indexed FAQ data for Maryland OLP AI Chat
This provides fast, local responses without requiring LLM API calls
"""

# The Five Domains of Action for Maryland OLP
FIVE_DOMAINS = [
    {
        "name": "Access to Nature",
        "description": "Ensuring all Maryland students have equitable access to outdoor learning experiences",
        "actions": [
            "Complete Landscape Assessment & Visual Map of Outdoor Learning Assets & Partners in Maryland"
        ],
        "recommendations": [
            "Create Mechanisms for Statewide Needs Monitoring with Data Collection & Analysis",
            "Formally Implement 'Outdoor Learning for All' in Maryland"
        ]
    },
    {
        "name": "College and Green Careers",
        "description": "Preparing students for success in college and the growing green career workforce",
        "actions": [
            "Develop a local AI search and modeling program to help construct learning and building tools specific for Maryland",
            "Revise or develop a new Conservation Careers Guide"
        ],
        "recommendations": [
            "Develop a new Career and Technology Education (CTE) pathway for students in 'Environmental Management, Sustainability and Technology'",
            "Maryland moves to adopt 4 science credits for graduation to keep pace with the need for advancing STEM areas"
        ]
    },
    {
        "name": "Networks",
        "description": "Building and strengthening environmental literacy networks across Maryland",
        "actions": [],
        "recommendations": [
            "Hire and onboard a qualified applicant for the Environmental Literacy Specialist position at MSDE before the end of the 2025-2026 school year",
            "Strengthen regional environmental literacy network hubs throughout the state of Maryland"
        ]
    },
    {
        "name": "School Sustainability",
        "description": "Supporting Local Education Agencies in reducing environmental impact of school buildings and grounds",
        "actions": [],
        "recommendations": [
            "Increase sustainable schools in Maryland"
        ]
    },
    {
        "name": "Environmental and Climate Literacy",
        "description": "Advancing environmental and climate education standards and teacher preparation",
        "actions": [
            "Investigate the alignment between the Community Schools Program and environmental literacy efforts",
            "Define a Climate Literate Student in Maryland"
        ],
        "recommendations": [
            "Establish a process to rename and update the Environmental Education in Maryland Public School (2010) to reflect current initiatives",
            "Strengthen and Incorporate Environmental Literacy in Maryland teacher preparation programs"
        ]
    }
]

FAQ_INDEX = {
    # Maryland OLP Overview
    "what is maryland olp": {
        "answer": "The Maryland Outdoor Learning Partnership (Maryland OLP) was established by Executive Order 01.01.2024.15 to ensure every young person in Maryland is empowered to access, conserve, and restore natural resources while preparing for a climate-ready future. Maryland was the first state in the nation to require environmental literacy for graduation (since 2011).\n\nOLP organizes its work around **five domains of action**:\n1. Access to Nature\n2. College and Green Careers\n3. Networks\n4. School Sustainability\n5. Environmental and Climate Literacy",
        "category": "overview",
        "related": ["five domains", "environmental literacy", "executive order"]
    },
    "what is environmental literacy": {
        "answer": "Environmental literacy is the ability to understand and make informed decisions about the environment and environmental issues. In Maryland, students must demonstrate environmental literacy to graduate, which includes understanding ecosystems, human impacts on the environment, and sustainable practices.",
        "category": "overview",
        "related": ["graduation requirements", "standards", "curriculum"]
    },

    # MWEE - Meaningful Watershed Educational Experience
    "what is mwee": {
        "answer": "A Meaningful Watershed Educational Experience (MWEE) is a multi-stage learning experience that includes classroom instruction and outdoor field investigations focused on local environmental issues. MWEEs help students develop environmental literacy through hands-on, place-based learning connected to the Chesapeake Bay watershed.",
        "category": "programs",
        "related": ["outdoor learning", "chesapeake bay", "field experience"]
    },
    "mwee requirements": {
        "answer": "Maryland requires all students to participate in a Meaningful Watershed Educational Experience (MWEE) before graduation. MWEEs must include: 1) Issue definition and background research, 2) Outdoor field investigation, 3) Action projects addressing environmental issues, and 4) Synthesis and reflection on learning.",
        "category": "requirements",
        "related": ["graduation", "outdoor learning", "environmental literacy"]
    },

    # Green Schools
    "what are green schools": {
        "answer": "Maryland Green Schools is a certification program recognizing schools that demonstrate environmental best practices and integrate environmental education across the curriculum. Schools work toward sustainable operations, outdoor learning spaces, and student environmental stewardship.",
        "category": "programs",
        "related": ["certification", "sustainability", "environmental education"]
    },
    "how to become green school": {
        "answer": "To become a Maryland Green School, schools must: 1) Form a Green School committee, 2) Complete a sustainability audit, 3) Implement environmental best practices, 4) Integrate environmental literacy across subjects, 5) Create outdoor learning opportunities, and 6) Submit an application to MAEOE for certification.",
        "category": "programs",
        "related": ["certification", "maeoe", "sustainability"]
    },

    # CTE Standards & Career Pathways
    "cte standards": {
        "answer": "Maryland's Career and Technical Education (CTE) standards provide content frameworks for career-focused programs. Environmental education connects to several CTE pathways including: Agriculture Science, Horticultural Science, Renewable Energy, and Marine Maintenance. Standards are available at marylandpublicschools.org/programs/pages/cte/standards.aspx",
        "category": "standards",
        "related": ["career pathways", "agriculture", "renewable energy"],
        "url": "https://marylandpublicschools.org/programs/pages/cte/standards.aspx"
    },
    "career pathways environmental": {
        "answer": "Environmental career pathways in Maryland CTE include: Renewable Energy, Agriculture Science, Horticultural Science, Marine Technology, and Construction trades with sustainability focus. These programs prepare students for green careers while meeting environmental literacy requirements.",
        "category": "careers",
        "related": ["cte", "green jobs", "workforce development"]
    },

    # Climate Education
    "climate education": {
        "answer": "Climate literacy is a key component of Maryland's environmental education framework. Students learn about climate systems, human impacts on climate, and climate solutions. The Environmental & Climate Literacy (ECL) workgroup develops recommendations for integrating climate education across grade levels.",
        "category": "curriculum",
        "related": ["environmental literacy", "climate literacy", "standards"]
    },
    "climate literacy definition": {
        "answer": "Climate literacy encompasses understanding of climate science, human-climate interactions, and the ability to make informed decisions about climate-related issues. Maryland integrates climate literacy within environmental literacy standards to prepare students for civic engagement and career readiness.",
        "category": "curriculum",
        "related": ["environmental literacy", "standards", "science"]
    },

    # Partners & Resources
    "dnr resources": {
        "answer": "Maryland Department of Natural Resources (DNR) offers educational resources including: wildlife and habitat programs, state park educational programs, Chesapeake Bay resources, hunting/fishing education, and environmental stewardship initiatives. Visit dnr.maryland.gov for full resources.",
        "category": "resources",
        "related": ["state parks", "wildlife", "chesapeake bay"],
        "url": "https://dnr.maryland.gov"
    },
    "chesapeake bay foundation": {
        "answer": "The Chesapeake Bay Foundation (CBF) is a key partner providing environmental education programs, field experiences, and curriculum resources focused on Bay restoration. CBF offers teacher professional development, student programs, and classroom resources aligned with Maryland standards.",
        "category": "partners",
        "related": ["mwee", "field experience", "professional development"]
    },

    # Contact Information
    "contact olp": {
        "answer": "Contact Maryland OLP:\n\nOlivia Wisner: olivia.wisner1@maryland.gov\nStephanie Tuckfield: stephanie.tuckfield1@maryland.gov\n\nThey coordinate environmental literacy initiatives and can connect you with resources and partner organizations.",
        "category": "contact",
        "related": ["get involved", "partners", "support"]
    },
    "who to contact": {
        "answer": "For Maryland OLP inquiries, contact:\n- Olivia Wisner: olivia.wisner1@maryland.gov\n- Stephanie Tuckfield: stephanie.tuckfield1@maryland.gov\n\nFor CTE Standards: Marquita Friday, Director of Career Programs\n- Phone: (410) 767-0183\n- Email: marquita.friday@maryland.gov",
        "category": "contact",
        "related": ["support", "partners", "resources"]
    },

    # Five Domains of Action
    "five domains": {
        "answer": "Maryland OLP organizes its work around **five domains of action**:\n\n**1. Access to Nature** - Ensuring all students have equitable access to outdoor learning\n\n**2. College and Green Careers** - Preparing students for success in the growing green workforce\n\n**3. Networks** - Building environmental literacy networks across Maryland\n\n**4. School Sustainability** - Reducing environmental impact of school buildings and grounds\n\n**5. Environmental and Climate Literacy** - Advancing education standards and teacher preparation\n\nEach domain has working groups developing specific actions and recommendations for 2025.",
        "category": "domains",
        "related": ["working groups", "recommendations", "olp mission"]
    },
    "domains": {
        "answer": "Maryland OLP organizes its work around **five domains of action**:\n\n**1. Access to Nature** - Ensuring all students have equitable access to outdoor learning\n\n**2. College and Green Careers** - Preparing students for success in the growing green workforce\n\n**3. Networks** - Building environmental literacy networks across Maryland\n\n**4. School Sustainability** - Reducing environmental impact of school buildings and grounds\n\n**5. Environmental and Climate Literacy** - Advancing education standards and teacher preparation",
        "category": "domains",
        "related": ["working groups", "recommendations", "olp mission"]
    },

    # Domain 1: Access to Nature
    "access to nature": {
        "answer": "**Access to Nature** is one of OLP's five domains of action, ensuring all Maryland students have equitable access to outdoor learning experiences.\n\n**Current Actions:**\n- Complete Landscape Assessment & Visual Map of Outdoor Learning Assets & Partners in Maryland\n\n**Recommendations:**\n- Create Mechanisms for Statewide Needs Monitoring with Data Collection & Analysis\n- Formally Implement 'Outdoor Learning for All' in Maryland\n\nKey priorities include expanding outdoor learning sites, transportation solutions, and removing barriers for underserved communities.",
        "category": "domains",
        "related": ["outdoor learning", "equity", "five domains"]
    },

    # Domain 2: College and Green Careers
    "college and green careers": {
        "answer": "**College and Green Careers** is one of OLP's five domains of action, preparing students for success in college and the growing green career workforce.\n\n**Current Actions:**\n- Develop a local AI search and modeling program for Maryland-specific learning tools\n- Revise or develop a new Conservation Careers Guide\n\n**Recommendations:**\n- Develop a new CTE pathway for 'Environmental Management, Sustainability and Technology'\n- Maryland moves to adopt 4 science credits for graduation\n\nThis domain connects environmental literacy with workforce development and career readiness.",
        "category": "domains",
        "related": ["cte", "green careers", "workforce", "five domains"]
    },
    "green careers": {
        "answer": "**College and Green Careers** focuses on preparing Maryland students for the growing green economy. Key initiatives include:\n\n- New CTE pathway in 'Environmental Management, Sustainability and Technology'\n- Updated Conservation Careers Guide with renewable energy, carbon reduction, and blue/green economy sectors\n- Youth apprenticeship opportunities with industry partners\n- Connections to P-Tech programs linking high schools with community colleges and careers\n\nModel programs exist at Western School of Environmental Science and Technology (Baltimore County) with certificates in Erosion & Sediment Control, EPA Watershed Academy, and GIS.",
        "category": "domains",
        "related": ["cte", "careers", "workforce development"]
    },

    # Domain 3: Networks
    "networks": {
        "answer": "**Networks** is one of OLP's five domains of action, building and strengthening environmental literacy connections across Maryland.\n\n**Recommendations:**\n- Hire and onboard a qualified Environmental Literacy Specialist at MSDE before end of 2025-2026 school year\n- Strengthen regional environmental literacy network hubs throughout Maryland\n\nStrong networks help coordinate resources, share best practices, and ensure environmental education is equitably implemented and sustainably funded statewide.",
        "category": "domains",
        "related": ["partnerships", "regional hubs", "five domains"]
    },

    # Domain 4: School Sustainability
    "school sustainability": {
        "answer": "**School Sustainability** is one of OLP's five domains of action, supporting Local Education Agencies in reducing environmental impact of school buildings and grounds.\n\n**Recommendations:**\n- Increase sustainable schools in Maryland\n\nThis domain connects to Maryland Green Schools certification and helps schools implement sustainable operations, outdoor learning spaces, and student environmental stewardship initiatives.",
        "category": "domains",
        "related": ["green schools", "sustainability", "five domains"]
    },
    "sustainable schools": {
        "answer": "**School Sustainability** focuses on reducing the environmental impact of Maryland schools. This includes:\n\n- Green building practices and energy efficiency\n- Waste reduction and recycling programs\n- Outdoor learning spaces and school gardens\n- Student-led sustainability initiatives\n- Connection to Maryland Green Schools certification\n\nLocal Education Agencies work to lessen environmental impact on local watersheds while creating hands-on learning opportunities.",
        "category": "domains",
        "related": ["green schools", "sustainability", "operations"]
    },

    # Domain 5: Environmental and Climate Literacy
    "environmental and climate literacy": {
        "answer": "**Environmental and Climate Literacy** is one of OLP's five domains of action, advancing education standards and teacher preparation.\n\n**Current Actions:**\n- Investigate alignment between Community Schools Program and environmental literacy\n- Define a Climate Literate Student in Maryland\n\n**Recommendations:**\n- Update the Environmental Education in Maryland Public School (2010) document\n- Strengthen Environmental Literacy in Maryland teacher preparation programs\n\nThis domain ensures all Maryland teachers have the training and support to implement environmental literacy standards.",
        "category": "domains",
        "related": ["standards", "teacher preparation", "climate literacy", "five domains"]
    },

    # Local-First AI
    "local first ai": {
        "answer": "Local-first AI means intelligence runs on your own devices or within your organization's infrastructure rather than distant cloud servers. Benefits include: 1) Privacy - data stays under your control, 2) Reliability - works offline, 3) Customization - trained on Maryland-specific resources. This approach supports FERPA/COPPA compliance by design.",
        "category": "technology",
        "related": ["privacy", "data security", "collaboration"]
    },
    "ai collaboration": {
        "answer": "AI-powered collaboration for Maryland OLP enables: matching partners with complementary resources, identifying collaboration opportunities, streamlining communication across 24 counties, and sharing anonymized patterns between districts without exposing raw data. This federated approach lets everyone benefit from collective intelligence while maintaining data privacy.",
        "category": "technology",
        "related": ["local first", "partners", "data sharing"]
    },

    # Professional Development
    "professional development": {
        "answer": "Maryland offers environmental literacy professional development through multiple partners including: MAEOE (Maryland Association for Environmental and Outdoor Education), Chesapeake Bay Foundation, DNR, and university programs. Opportunities include workshops, certifications, and ongoing learning communities for educators.",
        "category": "professional development",
        "related": ["training", "teachers", "certification"]
    },

    # Funding
    "funding grants": {
        "answer": "Funding opportunities for environmental education in Maryland include: NOAA B-WET grants for watershed education, Chesapeake Bay Trust grants, MAEOE mini-grants for educators, and various foundation grants. Check the Resources page for current opportunities.",
        "category": "funding",
        "related": ["grants", "b-wet", "chesapeake bay trust"]
    },
    "b-wet grants": {
        "answer": "Bay Watershed Education and Training (B-WET) grants are federal funding from NOAA supporting meaningful watershed educational experiences in the Chesapeake Bay region. Grants support schools and partners implementing MWEEs and environmental literacy programs.",
        "category": "funding",
        "related": ["noaa", "mwee", "federal funding"],
        "url": "https://www.noaa.gov/office-education/bwet"
    }
}

# Keywords to FAQ mapping for fuzzy matching
KEYWORD_MAP = {
    "olp": ["what is maryland olp", "contact olp", "five domains"],
    "eli": ["what is maryland olp", "what is environmental literacy"],
    "environmental literacy": ["what is environmental literacy", "environmental and climate literacy", "mwee requirements"],
    "mwee": ["what is mwee", "mwee requirements"],
    "watershed": ["what is mwee", "b-wet grants"],
    "green school": ["what are green schools", "how to become green school"],
    "certification": ["how to become green school", "professional development"],
    "climate": ["climate education", "climate literacy definition", "environmental and climate literacy"],
    "career": ["college and green careers", "green careers", "cte standards"],
    "cte": ["cte standards", "college and green careers"],
    "job": ["college and green careers", "green careers"],
    "workforce": ["college and green careers", "green careers"],
    "dnr": ["dnr resources"],
    "natural resources": ["dnr resources"],
    "chesapeake": ["chesapeake bay foundation", "what is mwee", "b-wet grants"],
    "bay": ["chesapeake bay foundation", "what is mwee"],
    "contact": ["contact olp", "who to contact"],
    "email": ["contact olp", "who to contact"],
    "help": ["contact olp", "who to contact"],
    "funding": ["funding grants", "b-wet grants"],
    "grant": ["funding grants", "b-wet grants"],
    "money": ["funding grants", "b-wet grants"],
    "training": ["professional development"],
    "teacher": ["professional development", "environmental and climate literacy"],
    "pd": ["professional development"],
    "working group": ["five domains", "access to nature", "college and green careers"],
    "recommendation": ["five domains", "access to nature"],
    "2025": ["five domains", "access to nature"],
    "access": ["access to nature"],
    "nature": ["access to nature"],
    "outdoor": ["access to nature", "what is mwee"],
    "sustainable": ["sustainable schools", "school sustainability"],
    "sustainability": ["sustainable schools", "school sustainability", "what are green schools"],
    "ai": ["local first ai", "ai collaboration", "college and green careers"],
    "local": ["local first ai"],
    "privacy": ["local first ai"],
    "partner": ["ai collaboration", "chesapeake bay foundation", "networks"],
    "collaborate": ["ai collaboration", "networks"],
    "network": ["networks"],
    "standard": ["cte standards", "what is environmental literacy", "environmental and climate literacy"],
    "graduation": ["mwee requirements", "what is environmental literacy"],
    "require": ["mwee requirements", "what is environmental literacy"],
    "domain": ["five domains", "what is maryland olp"],
    "five": ["five domains"],
    "action": ["five domains", "access to nature"],
    "college": ["college and green careers"],
    "green": ["college and green careers", "green careers", "what are green schools"]
}


def find_best_match(query: str) -> dict:
    """Find the best FAQ match for a user query"""
    query_lower = query.lower().strip()

    # Direct match
    if query_lower in FAQ_INDEX:
        return FAQ_INDEX[query_lower]

    # Check for keyword matches
    matched_faqs = []
    for keyword, faq_keys in KEYWORD_MAP.items():
        if keyword in query_lower:
            matched_faqs.extend(faq_keys)

    # Return most common match or first match
    if matched_faqs:
        # Count occurrences and return most relevant
        from collections import Counter
        counts = Counter(matched_faqs)
        best_key = counts.most_common(1)[0][0]
        return FAQ_INDEX[best_key]

    # No match found
    return None


def get_all_categories() -> list:
    """Get list of all FAQ categories"""
    categories = set()
    for faq in FAQ_INDEX.values():
        categories.add(faq.get("category", "general"))
    return sorted(list(categories))


def get_faqs_by_category(category: str) -> list:
    """Get all FAQs in a specific category"""
    return [
        {"question": key, **value}
        for key, value in FAQ_INDEX.items()
        if value.get("category") == category
    ]
