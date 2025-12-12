# BUILD-PLAN.md
## Maryland OLP Site - Source of Truth

**Last Updated:** 2025-12-12
**Purpose:** Living document tracking project state, decisions, session logs, and roadmap for human/AI continuity.

---

## PROJECT OVERVIEW

**What:** Maryland Outdoor Learning Partnership (OLP) website with AI-powered chat assistant
**Who:** Environmental education stakeholders in Maryland's 24 school districts
**Why:** Support Maryland's first-in-nation environmental literacy graduation requirement (since 2011)

---

## CURRENT PROJECT STRUCTURE

```
olp-site-fun-maryland/
├── .git/                    # Git repository
├── .gitignore               # Root gitignore - ignores docs, python cruft
├── BUILD-PLAN.md            # This file - source of truth
├── docker-compose.yml       # [NEW] Container orchestration
│
├── index.html               # [CORE] Main landing page (~2270 lines)
├── ai-chat.html             # [CORE] AI chat interface (~1195 lines)
├── resources.html           # [CORE] Resources page (large file)
│
├── backend/                 # [CORE] Python Flask API
│   ├── Dockerfile           # [NEW] Container build instructions
│   ├── .gitignore           # Backend-specific ignores
│   ├── .env                 # [SECRET] Active environment config
│   ├── .env.example         # Template for env vars
│   ├── app.py               # [CORE] Flask API server (479 lines)
│   ├── faq_data.py          # [CORE] FAQ index & matching (332 lines)
│   ├── requirements.txt     # Python dependencies
│   ├── README.md            # Backend documentation
│   ├── LOCAL_AI_SETUP.md    # Local AI setup guide (detailed)
│   ├── Modelfile            # [OPTIONAL] Ollama custom model config
│   ├── __pycache__/         # [IGNORED] Python cache
│   └── venv/                # [IGNORED] Virtual environment
│
└── [UNTRACKED DOCUMENTS]    # .docx/.pdf working files (ignored by git)
```

---

## FILE AUDIT & STATUS

### NECESSARY FILES (Keep)

| File | Purpose | Status |
|------|---------|--------|
| `index.html` | Main landing page - hero, mission, data dashboard, domains, standards, resources, partners, CTA, footer | Core |
| `ai-chat.html` | AI chat interface - connects to backend or falls back to local FAQ | Core |
| `resources.html` | Dedicated resources page with categorized links | Core |
| `backend/app.py` | Flask API - PocketFlow-style nodes, multi-LLM support (ollama, llamacpp, api, hybrid, faq modes) | Core |
| `backend/faq_data.py` | Pre-indexed FAQ database - FIVE_DOMAINS, FAQ_INDEX, KEYWORD_MAP, find_best_match() | Core |
| `backend/requirements.txt` | Python deps: pocketflow, flask, flask-cors, python-dotenv, openai, requests, anthropic | Core |
| `backend/.env.example` | Template showing all config options | Core |
| `backend/README.md` | API documentation and deployment guides | Keep |
| `backend/LOCAL_AI_SETUP.md` | Detailed local AI setup for M3 Pro | Keep (useful) |
| `.gitignore` | Root ignore for docs, python, IDE files | Core |
| `backend/.gitignore` | Backend-specific ignores | Core |

### OPTIONAL FILES

| File | Reason |
|------|--------|
| `backend/Modelfile` | Optional Ollama customization - not tracked | Optional |

### UNTRACKED (Intentionally Ignored)

| Files | Status |
|-------|--------|
| `*.docx` (10+ files) | Working documents - kept local only |
| `*.pdf` (2 files) | Reference materials - kept local only |
| `files.zip` | Archive - local only |
| `backend/.env` | Secrets - never commit |
| `backend/venv/` | Python environment - recreate via requirements.txt |
| `backend/__pycache__/` | Compiled Python - auto-generated |

---

## ARCHITECTURE DECISIONS

### Frontend
- **Pure HTML/CSS/JS** - No build step, static hosting compatible
- **Self-contained CSS** - All styles inline in each HTML file
- **Progressive enhancement** - Works without JS, enhanced with JS

### Backend
- **Flask API** - Simple, Python-based
- **PocketFlow pattern** - Node-based flow for extensibility
- **Multi-LLM fallback chain** - Local (Ollama/llama.cpp) → Cheap API (OpenRouter) → Premium API (Anthropic/OpenAI) → FAQ
- **FAQ-first** - Pre-indexed responses for common questions (no API cost)

### AI Strategy
- **Local-first** - Privacy, offline capability, no per-query costs
- **Recommended model** - GPT-OSS 20B or Qwen3 30B for M3 Pro with 36GB RAM
- **Fallback chain** - Ensures response even if local AI unavailable

### Deployment Strategy
- **Container isolation** - Backend runs in Docker for security
- **Tailscale Funnel** - Secure tunnel to expose local container to internet
- **Cold starts OK** - Not production yet, container can sleep when not in use
- **Data stays local** - Your machine, your data, your control

---

## CONTAINER SETUP

### Quick Start
```bash
# Build and run
docker compose up -d

# Check status
docker ps

# View logs
docker logs olp-backend

# Stop
docker compose down
```

### Container Details
- **Image:** `olp-site-fun-maryland-backend`
- **Container:** `olp-backend`
- **Port:** 5000
- **User:** Non-root `olp` user (security)
- **Host access:** Can reach host Ollama via `host.docker.internal:11434`

### Connecting to Host Ollama
If running Ollama on your Mac (not in container):
```bash
# Start Ollama on host
ollama serve

# Container can reach it at http://host.docker.internal:11434
```

---

## GIT CONFIGURATION

### What's Tracked
- All HTML files (frontend)
- All backend Python code
- Configuration templates (.env.example)
- Documentation (README.md, LOCAL_AI_SETUP.md)
- This BUILD-PLAN.md

### What's Ignored
- Working documents (*.docx, *.pdf)
- Secrets (backend/.env)
- Dependencies (venv/, node_modules/)
- Cache (__pycache__/)
- IDE files (.vscode/, .idea/)
- OS files (.DS_Store)

---

## SESSION LOG

### Session: 2025-12-12

**Objective:** Audit project structure, establish source of truth, containerize backend

**Actions Taken:**
1. Reviewed full project structure
2. Read all core files to understand architecture
3. Created root `.gitignore` to ignore working documents
4. Created `BUILD-PLAN.md` as living documentation
5. Discovered existing `maryland-ai` project at `/Users/willf/00_maryland-ai-starter/maryland-ai/` (more complex, has RAG/auth)
6. Decided to keep projects separate - OLP is simple public FAQ, maryland-ai is internal tools
7. Created `backend/Dockerfile` for container isolation
8. Created `docker-compose.yml` for easy startup
9. Built and tested container - working on port 5000

**Decisions Made:**
- Keep OLP simple and separate from maryland-ai stack
- Use Docker container for backend isolation (security)
- Plan to use Tailscale Funnel for secure public access
- Cold starts acceptable (not production yet)
- Data stays local on your machine

**Files Changed:**
- `[NEW] .gitignore` - Root level ignore file
- `[NEW] BUILD-PLAN.md` - This file
- `[NEW] backend/Dockerfile` - Container build instructions
- `[NEW] docker-compose.yml` - Container orchestration

**Container Status:**
- Image: `olp-site-fun-maryland-backend` (built)
- Container: `olp-backend` (running)
- Port: 5000
- Test: `curl http://localhost:5000/` returns healthy

**Next Steps:**
- [ ] Install Tailscale: `brew install tailscale`
- [ ] Configure Tailscale Funnel to expose port 5000
- [ ] Update `ai-chat.html` API_URL with Tailscale domain
- [ ] Test end-to-end with frontend on GitHub Pages
- [ ] Consider: consolidate duplicate CSS across HTML files?

---

## PENDING DECISIONS

### Needs Discussion

1. **CSS Duplication**
   - Each HTML file has full CSS inline (~1400+ lines each)
   - Could extract to shared `styles.css`
   - Trade-off: Simplicity vs. maintainability

2. **Component Extraction**
   - Nav and footer are duplicated across pages
   - Could use JS includes or build step
   - Trade-off: Zero-dependency vs. DRY

3. **Backend Deployment** (DECIDED)
   - Using Docker + Tailscale Funnel for local-first deployment
   - Container runs on your Mac, Tailscale exposes it securely
   - May need CORS config updates for production domain

4. **Document Management**
   - Working .docx files are in project root
   - Consider: dedicated `docs/` folder (still gitignored)?

---

## HOW TO USE THIS DOCUMENT

### For Humans
- Check "SESSION LOG" for recent changes
- Check "PENDING DECISIONS" for open questions
- Update after each work session

### For AI (Claude Code, etc.)
- Read this file FIRST to understand project state
- Check "ARCHITECTURE DECISIONS" before suggesting changes
- Add new session entries with: date, objective, actions, decisions, files changed, next steps
- Keep entries detailed enough to rebuild context in a new session

### When Starting a New Session
1. Read BUILD-PLAN.md
2. Check git status for uncommitted changes
3. Review last session's "Next Steps"
4. Add new session entry before starting work

---

## COMMIT CONVENTIONS

Format: `<type>: <description>`

Types:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `style:` - Formatting (no code change)
- `refactor:` - Code restructure (no feature change)
- `chore:` - Maintenance tasks
