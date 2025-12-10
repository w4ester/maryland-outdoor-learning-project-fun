"""
Maryland OLP AI Chat Backend
A simple Flask API using PocketFlow for chat orchestration
Supports: Local Ollama, llama.cpp, API (OpenRouter/Anthropic/OpenAI), FAQ fallback
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

# Import FAQ data
from faq_data import find_best_match, FAQ_INDEX, FIVE_DOMAINS, KEYWORD_MAP

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# ============================================
# Configuration
# ============================================

LLM_MODE = os.environ.get("LLM_MODE", "faq")  # faq, ollama, llamacpp, api, hybrid

# Ollama settings
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "gpt-oss:20b")

# llama.cpp settings
LLAMACPP_URL = os.environ.get("LLAMACPP_URL", "http://localhost:8080")

# API settings
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_MODEL = os.environ.get("OPENROUTER_MODEL", "deepseek/deepseek-r1-distill-llama-8b")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

# System prompt for LLM
SYSTEM_PROMPT = """You are the Maryland Outdoor Learning Partnership (OLP) AI Assistant.
You help educators, partners, and community members learn about environmental literacy in Maryland.

Key facts:
- Maryland was the first state to require environmental literacy for graduation (since 2011)
- OLP was established by Executive Order 01.01.2024.15
- OLP has five domains of action: Access to Nature, College & Green Careers, Networks, School Sustainability, Environmental & Climate Literacy
- MWEE = Meaningful Watershed Educational Experience (required for graduation)
- Contact: olivia.wisner1@maryland.gov and stephanie.tuckfield1@maryland.gov

Be helpful, accurate, and concise. Focus on Maryland-specific environmental education information."""


# ============================================
# LLM Provider Functions
# ============================================

def call_ollama(query: str) -> str | None:
    """Call local Ollama server"""
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": f"{SYSTEM_PROMPT}\n\nUser: {query}\n\nAssistant:",
                "stream": False
            },
            timeout=60
        )
        if response.ok:
            return response.json().get("response", "").strip()
    except Exception as e:
        print(f"Ollama error: {e}")
    return None


def call_llamacpp(query: str) -> str | None:
    """Call local llama.cpp server (OpenAI-compatible API)"""
    try:
        response = requests.post(
            f"{LLAMACPP_URL}/v1/chat/completions",
            json={
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": query}
                ],
                "max_tokens": 1024
            },
            timeout=60
        )
        if response.ok:
            return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"llama.cpp error: {e}")
    return None


def call_openrouter(query: str) -> str | None:
    """Call OpenRouter API (cheap models like DeepSeek)"""
    if not OPENROUTER_API_KEY:
        return None
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": OPENROUTER_MODEL,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": query}
                ]
            },
            timeout=30
        )
        if response.ok:
            return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"OpenRouter error: {e}")
    return None


def call_anthropic(query: str) -> str | None:
    """Call Anthropic Claude API"""
    if not ANTHROPIC_API_KEY:
        return None
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "Content-Type": "application/json"
            },
            json={
                "model": "claude-3-haiku-20240307",
                "max_tokens": 1024,
                "system": SYSTEM_PROMPT,
                "messages": [{"role": "user", "content": query}]
            },
            timeout=30
        )
        if response.ok:
            return response.json()["content"][0]["text"].strip()
    except Exception as e:
        print(f"Anthropic error: {e}")
    return None


def call_openai(query: str) -> str | None:
    """Call OpenAI API"""
    if not OPENAI_API_KEY:
        return None
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": query}
                ]
            },
            timeout=30
        )
        if response.ok:
            return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"OpenAI error: {e}")
    return None


def get_llm_response(query: str) -> tuple[str | None, str]:
    """Get response based on configured LLM_MODE with fallback chain"""

    if LLM_MODE == "ollama":
        result = call_ollama(query)
        if result:
            return result, "ollama"

    elif LLM_MODE == "llamacpp":
        result = call_llamacpp(query)
        if result:
            return result, "llamacpp"

    elif LLM_MODE == "api":
        # Try OpenRouter first (cheapest), then Anthropic, then OpenAI
        result = call_openrouter(query)
        if result:
            return result, "openrouter"
        result = call_anthropic(query)
        if result:
            return result, "anthropic"
        result = call_openai(query)
        if result:
            return result, "openai"

    elif LLM_MODE == "hybrid":
        # Full fallback chain: local → cheap API → premium API
        result = call_ollama(query)
        if result:
            return result, "ollama"
        result = call_llamacpp(query)
        if result:
            return result, "llamacpp"
        result = call_openrouter(query)
        if result:
            return result, "openrouter"
        result = call_anthropic(query)
        if result:
            return result, "anthropic"
        result = call_openai(query)
        if result:
            return result, "openai"

    return None, "none"


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
            "has_faq": shared.get("has_faq_match", False),
            "faq_match": shared.get("faq_match"),
            "has_llm": shared.get("has_llm_response", False),
            "llm_response": shared.get("llm_response"),
            "llm_source": shared.get("llm_source"),
            "query": shared.get("query", "")
        }

    def exec(self, data):
        # Priority 1: FAQ match
        if data["has_faq"] and data["faq_match"]:
            faq = data["faq_match"]
            response = {
                "answer": faq["answer"],
                "category": faq.get("category", "general"),
                "related": faq.get("related", []),
                "url": faq.get("url"),
                "source": "faq"
            }

        # Priority 2: LLM response
        elif data["has_llm"] and data["llm_response"]:
            response = {
                "answer": data["llm_response"],
                "category": "ai_generated",
                "related": [],
                "source": data["llm_source"]
            }

        # Priority 3: Fallback
        else:
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


class LLMNode(Node):
    """Call LLM for questions not in FAQ"""

    def prep(self, shared):
        return {
            "query": shared.get("query", ""),
            "has_faq": shared.get("has_faq_match", False)
        }

    def exec(self, data):
        # Skip LLM if FAQ already answered
        if data["has_faq"]:
            return None

        # Try to get LLM response
        response, source = get_llm_response(data["query"])
        return {"response": response, "source": source}

    def post(self, shared, result):
        if result and result["response"]:
            shared["llm_response"] = result["response"]
            shared["llm_source"] = result["source"]
            shared["has_llm_response"] = True
        else:
            shared["has_llm_response"] = False
        return result


class ChatFlow:
    """Orchestrate the chat nodes following PocketFlow pattern"""

    def __init__(self):
        self.faq_node = FAQSearchNode()
        self.llm_node = LLMNode()
        self.formatter_node = ResponseFormatterNode()

    def run(self, query):
        # Shared state passed between nodes
        shared = {"query": query}

        # Step 1: Try FAQ search first
        self.faq_node.run(shared)

        # Step 2: If no FAQ match, try LLM
        if not shared.get("has_faq_match") and LLM_MODE != "faq":
            self.llm_node.run(shared)

        # Step 3: Format response
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
        "version": "2.0.0",
        "llm_mode": LLM_MODE,
        "ollama_model": OLLAMA_MODEL if LLM_MODE in ["ollama", "hybrid"] else None,
        "has_openrouter": bool(OPENROUTER_API_KEY),
        "has_anthropic": bool(ANTHROPIC_API_KEY),
        "has_openai": bool(OPENAI_API_KEY)
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
