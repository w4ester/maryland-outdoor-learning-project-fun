# Maryland OLP AI Chat Backend

A simple Flask API using PocketFlow-style patterns for the AI chat interface.

## Features

- **Pre-indexed FAQ responses** - Fast, local-first answers without API calls
- **PocketFlow architecture** - Node-based flow for extensibility
- **Five Domains of Action** - OLP's organizational framework
- **Keyword matching** - Fuzzy search for related topics

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run the server
python app.py
```

Server runs at `http://localhost:5000`

## API Endpoints

### Chat
```
POST /api/chat
Body: {"message": "What is MWEE?"}
Response: {"answer": "...", "category": "...", "related": [...]}
```

### Get Five Domains
```
GET /api/domains
Response: {"domains": [...]}
```

### List FAQ Topics
```
GET /api/faq
Response: {"topics": [...]}
```

### Get Specific Topic
```
GET /api/faq/mwee
Response: {"answer": "...", "category": "..."}
```

### Suggest Topics
```
GET /api/suggest?q=climate
Response: {"suggestions": ["climate education", "climate literacy definition"]}
```

## Deployment

### Railway
1. Connect GitHub repo
2. Set root directory to `/backend`
3. Railway auto-detects Flask

### Render
1. Create new Web Service
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python app.py`

### Vercel (Serverless)
Create `vercel.json`:
```json
{
  "builds": [{"src": "app.py", "use": "@vercel/python"}],
  "routes": [{"src": "/(.*)", "dest": "app.py"}]
}
```

## Adding More FAQs

Edit `faq_data.py`:

1. Add entry to `FAQ_INDEX`:
```python
"new topic": {
    "answer": "Your answer here...",
    "category": "category_name",
    "related": ["related topic 1", "related topic 2"],
    "url": "https://optional-link.com"  # optional
}
```

2. Add keywords to `KEYWORD_MAP`:
```python
"keyword": ["new topic", "other related topic"]
```

## Future Enhancements

- [ ] Connect to OpenAI/Anthropic for dynamic responses
- [ ] RAG with Maryland resource documents
- [ ] User feedback collection
- [ ] Analytics on common questions
