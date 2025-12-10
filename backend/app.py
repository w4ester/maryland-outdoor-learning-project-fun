"""
Maryland OLP AI Chat Backend
A simple Flask API using PocketFlow for chat orchestration
with pre-indexed FAQ responses for fast, local-first responses
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Import FAQ data
from faq_data import find_best_match, FAQ_INDEX, FIVE_DOMAINS, KEYWORD_MAP

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests


# ============================================
# PocketFlow-style Node Classes (simplified)
# ============================================

class Node:
    """Base node class following PocketFlow pattern"""
    def __init__(self):
        self.params = {}
        self.successors = {}

    def prep(self, shared):
        """Prepare step - gather inputs"""
        pass

    def exec(self, prep_result):
        """Execute step - main logic"""
        pass

    def post(self, shared, exec_result):
        """Post step - handle outputs"""
        return exec_result

    def run(self, shared):
        prep_result = self.prep(shared)
        exec_result = self.exec(prep_result)
        return self.post(shared, exec_result)


class FAQSearchNode(Node):
    """Search pre-indexed FAQ data for matching responses"""

    def prep(self, shared):
        return shared.get("query", "")

    def exec(self, query):
        if not query:
            return None

        # Try to find a match in FAQ index
        result = find_best_match(query)
        return result

    def post(self, shared, result):
        if result:
            shared["faq_match"] = result
            shared["has_faq_match"] = True
        else:
            shared["has_faq_match"] = False
        return result


class ResponseFormatterNode(Node):
    """Format the response for the chat interface"""

    def prep(self, shared):
        return {
            "has_match": shared.get("has_faq_match", False),
            "faq_match": shared.get("faq_match"),
            "query": shared.get("query", "")
        }

    def exec(self, data):
        if data["has_match"] and data["faq_match"]:
            faq = data["faq_match"]
            response = {
                "answer": faq["answer"],
                "category": faq.get("category", "general"),
                "related": faq.get("related", []),
                "url": faq.get("url"),
                "source": "faq"
            }
        else:
            # No match - provide helpful fallback
            response = {
                "answer": f"I don't have specific information about '{data['query']}' in my knowledge base yet. Here are some things I can help with:\n\n" +
                         "- **Five Domains of OLP**: Access to Nature, College & Green Careers, Networks, School Sustainability, Environmental & Climate Literacy\n" +
                         "- **Programs**: MWEE, Green Schools, CTE pathways\n" +
                         "- **Resources**: Funding, professional development, curriculum\n" +
                         "- **Contact info**: How to reach Maryland OLP team\n\n" +
                         "Try asking about one of these topics, or contact the OLP team directly:\n" +
                         "olivia.wisner1@maryland.gov or stephanie.tuckfield1@maryland.gov",
                "category": "fallback",
                "related": ["five domains", "contact olp", "what is maryland olp"],
                "source": "fallback"
            }
        return response


class ChatFlow:
    """Orchestrate the chat nodes following PocketFlow pattern"""

    def __init__(self):
        self.faq_node = FAQSearchNode()
        self.formatter_node = ResponseFormatterNode()

    def run(self, query):
        # Shared state passed between nodes
        shared = {"query": query}

        # Run FAQ search
        self.faq_node.run(shared)

        # Format response
        response = self.formatter_node.run(shared)

        return response


# Initialize the chat flow
chat_flow = ChatFlow()


# ============================================
# API Routes
# ============================================

@app.route("/")
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Maryland OLP AI Chat",
        "version": "1.0.0"
    })


@app.route("/api/chat", methods=["POST"])
def chat():
    """Main chat endpoint"""
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message required"}), 400

    query = data["message"]

    # Run through PocketFlow chat
    response = chat_flow.run(query)

    return jsonify(response)


@app.route("/api/domains", methods=["GET"])
def get_domains():
    """Get the five domains of action"""
    return jsonify({
        "domains": FIVE_DOMAINS
    })


@app.route("/api/faq", methods=["GET"])
def get_faq_list():
    """Get list of available FAQ topics"""
    topics = []
    for key, value in FAQ_INDEX.items():
        topics.append({
            "topic": key,
            "category": value.get("category", "general")
        })
    return jsonify({"topics": topics})


@app.route("/api/faq/<topic>", methods=["GET"])
def get_faq_topic(topic):
    """Get specific FAQ topic"""
    topic_lower = topic.lower().replace("-", " ")

    if topic_lower in FAQ_INDEX:
        return jsonify(FAQ_INDEX[topic_lower])

    # Try keyword search
    result = find_best_match(topic_lower)
    if result:
        return jsonify(result)

    return jsonify({"error": "Topic not found"}), 404


@app.route("/api/suggest", methods=["GET"])
def suggest_topics():
    """Suggest related topics based on partial query"""
    query = request.args.get("q", "").lower()

    if not query:
        return jsonify({"suggestions": []})

    suggestions = []

    # Check keywords
    for keyword, faq_keys in KEYWORD_MAP.items():
        if query in keyword or keyword in query:
            for key in faq_keys:
                if key not in suggestions:
                    suggestions.append(key)

    # Limit to 5 suggestions
    return jsonify({"suggestions": suggestions[:5]})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
