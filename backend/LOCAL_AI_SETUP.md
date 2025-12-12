# Maryland OLP AI Chat - Local AI Setup Guide
*Updated: December 10, 2025*

## Hardware: M3 Pro with 36GB Unified Memory

**Excellent specs!** With 36GB unified memory, you can run:
- Models up to ~30GB comfortably
- MoE (Mixture of Experts) models efficiently
- Multiple smaller models simultaneously

---

## Option 1: Ollama (Easiest Local Setup)

### Cold Start (5 minutes)

```bash
# Install Ollama
brew install ollama
# Or download from: https://ollama.com/download/mac

# Start service
ollama serve

# Pull recommended model (new terminal)
ollama pull gpt-oss:20b
```

### Best Models for 36GB RAM (December 2025)

| Model | Command | Size | Context | Best For |
|-------|---------|------|---------|----------|
| **GPT-OSS 20B** | `ollama pull gpt-oss:20b` | 14GB | 128K | Reasoning, coding, chain-of-thought |
| **Qwen3 30B MoE** | `ollama pull qwen3:30b` | 19GB | 256K | Best efficiency, rivals 72B quality |
| **Qwen3 8B** | `ollama pull qwen3:8b` | 5.2GB | 40K | Fast general purpose |
| **Qwen3 4B** | `ollama pull qwen3:4b` | 2.5GB | 256K | Rivals Qwen2.5-72B performance! |
| DeepSeek-R1 8B | `ollama pull deepseek-r1:8b` | ~5GB | 128K | Reasoning focused |
| Qwen3-Coder | `ollama pull qwen3-coder` | varies | 256K | Code generation |

### Why These Models?

**GPT-OSS 20B** (OpenAI, Apache 2.0 license)
- Only needs 16GB RAM thanks to MXFP4 quantization
- Full chain-of-thought access for transparency
- Configurable reasoning effort (low/medium/high)
- ~82 tokens/sec on M2 MacBook Pro
- *Source: [OpenAI GPT-OSS](https://openai.com/index/introducing-gpt-oss/)*

**Qwen3 30B MoE** (Alibaba)
- Only ~3B parameters active per token (efficient!)
- Outperforms QwQ-32B with 10x fewer active params
- 256K context window
- *Source: [Qwen3 Blog](https://qwenlm.github.io/blog/qwen3/)*

**Qwen3 4B** (Tiny but mighty)
- "Rivals the performance of Qwen2.5-72B-Instruct"
- Only 2.5GB download
- Great for testing and low-latency needs
- *Source: [Ollama Qwen3](https://ollama.com/library/qwen3)*

---

## Option 2: llama.cpp with GGUF (Most Control)

### Setup

```bash
# Clone and build with Metal GPU support
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
cmake -B build -DLLAMA_METAL=on -DCMAKE_BUILD_TYPE=Release
cmake --build build -j

# Run GPT-OSS directly from Hugging Face
./build/bin/llama-server \
  -hf ggml-org/gpt-oss-20b-GGUF \
  -c 0 \
  --jinja \
  -ngl 99
```

### Best GGUF Sources

| Source | Models | Notes |
|--------|--------|-------|
| [ggml-org/gpt-oss-20b-GGUF](https://huggingface.co/ggml-org/gpt-oss-20b-GGUF) | GPT-OSS | Official, 101K+ downloads |
| [bartowski](https://huggingface.co/bartowski) | Qwen3, Llama, etc | High quality quants |
| [unsloth](https://huggingface.co/unsloth/gpt-oss-20b-GGUF) | GPT-OSS | Optimized versions |
| [lmstudio-community](https://huggingface.co/lmstudio-community) | Various | LM Studio compatible |

### Quantization Guide

| Quant | Quality | Size vs Original | Recommended |
|-------|---------|------------------|-------------|
| Q8_0 | Best | ~100% | If RAM allows |
| Q6_K | Excellent | ~75% | Great balance |
| **Q4_K_M** | Very Good | ~50% | **Default choice** |
| Q4_K_S | Good | ~45% | Save more RAM |

*Source: [llama.cpp GitHub](https://github.com/ggml-org/llama.cpp)*

---

## Option 3: API-Based (Pay per Use)

### Current Pricing (December 2025)

#### Cheapest Options

| Provider | Model | Input/1M | Output/1M | Notes |
|----------|-------|----------|-----------|-------|
| **OpenRouter** | DeepSeek R1 8B | $0.03 | $0.13 | Incredible value |
| **OpenRouter** | DeepSeek R1 70B | $0.03 | $0.13 | Same price, better |
| Anthropic | Claude Haiku 3 | $0.25 | $1.25 | Very capable |
| OpenAI | GPT-4o-mini | $0.60 | $2.40 | Good balance |

#### Premium Options

| Provider | Model | Input/1M | Output/1M | Notes |
|----------|-------|----------|-----------|-------|
| Anthropic | Claude Sonnet 4.5 | $3.00 | $15.00 | Balanced |
| Anthropic | Claude Opus 4.5 | $5.00 | $25.00 | Most capable |
| OpenAI | GPT-4o | $5.00 | $20.00 | Flagship |
| OpenRouter | DeepSeek V3.1 | $0.21 | $0.32 | 671B params |

### Cost Per Message

Typical: ~500 input + ~300 output tokens

| Model | Cost/Message | 1000 Messages |
|-------|--------------|---------------|
| DeepSeek R1 (OpenRouter) | $0.00005 | **$0.05** |
| Claude Haiku 3 | $0.0005 | $0.50 |
| GPT-4o-mini | $0.001 | $1.00 |
| GPT-4o | $0.009 | $9.00 |

*Sources: [OpenAI Pricing](https://openai.com/api/pricing/), [Claude Pricing](https://www.anthropic.com/pricing), [OpenRouter](https://openrouter.ai/models)*

---

## Option 4: Hybrid Mode (Recommended)

```
User Message
     │
     ▼
┌──────────────────────┐
│ 1. Local (Ollama)    │ ──► GPT-OSS 20B or Qwen3
└──────────┬───────────┘     Free, private, fast
           │ (if unavailable)
           ▼
┌──────────────────────┐
│ 2. Cheap API         │ ──► DeepSeek R1 ($0.03/1M)
└──────────┬───────────┘
           │ (if unavailable)
           ▼
┌──────────────────────┐
│ 3. Premium API       │ ──► Claude/GPT-4o
└──────────┬───────────┘
           │ (if unavailable)
           ▼
┌──────────────────────┐
│ 4. FAQ Fallback      │ ──► Pre-indexed answers
└──────────────────────┘
```

### Configuration

```bash
# .env file
LLM_MODE=hybrid

# Local (primary)
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=gpt-oss:20b
# Or for llama.cpp:
# LLAMACPP_URL=http://localhost:8080

# Cheap API fallback
OPENROUTER_API_KEY=sk-or-your-key
OPENROUTER_MODEL=deepseek/deepseek-r1-distill-llama-8b

# Premium fallback
ANTHROPIC_API_KEY=sk-ant-your-key
```

---

## Option 5: Subscription Tiers

| Tier | Monthly | LLM Access |
|------|---------|------------|
| **Free** | $0 | FAQ only |
| **Basic** | $5 | Local + DeepSeek API |
| **Pro** | $20 | Claude Sonnet / GPT-4o |
| **Enterprise** | Custom | Dedicated instance |

---

## Quick Start Commands

### Recommended: GPT-OSS 20B
```bash
# Install & start Ollama
brew install ollama && ollama serve &

# Pull GPT-OSS (14GB download)
ollama pull gpt-oss:20b

# Test it
ollama run gpt-oss:20b "What are Maryland's environmental literacy requirements?"

# Start backend
cd backend
pip install -r requirements.txt
export LLM_MODE=ollama
export OLLAMA_MODEL=gpt-oss:20b
python app.py
```

### Alternative: Qwen3 30B (more efficient)
```bash
ollama pull qwen3:30b
ollama run qwen3:30b "Explain MWEE in Maryland education"
```

### llama.cpp Direct
```bash
# One command to download and run
cd llama.cpp
./build/bin/llama-server -hf ggml-org/gpt-oss-20b-GGUF -ngl 99 --jinja
# API at http://localhost:8080
```

---

## Model Comparison Summary

| Model | Size | Speed | Quality | Local Cost |
|-------|------|-------|---------|------------|
| **GPT-OSS 20B** | 14GB | ~80 tok/s | Excellent | Free |
| **Qwen3 30B MoE** | 19GB | ~40 tok/s | Excellent | Free |
| Qwen3 8B | 5GB | ~100 tok/s | Very Good | Free |
| Qwen3 4B | 2.5GB | ~150 tok/s | Good (rivals 72B!) | Free |
| DeepSeek R1 API | - | Fast | Excellent | $0.03/1M |

**For your 36GB M3 Pro: GPT-OSS 20B or Qwen3 30B are ideal choices.**

---

## Sources

- [OpenAI GPT-OSS Announcement](https://openai.com/index/introducing-gpt-oss/)
- [GPT-OSS with llama.cpp Guide](https://simonwillison.net/2025/Aug/19/gpt-oss-with-llama-cpp/)
- [Qwen3 Blog](https://qwenlm.github.io/blog/qwen3/)
- [Ollama Library](https://ollama.com/library)
- [llama.cpp GitHub](https://github.com/ggml-org/llama.cpp)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenAI Pricing](https://openai.com/api/pricing/)
- [Claude Pricing](https://www.anthropic.com/pricing)
- [Best Ollama Models 2025](https://collabnix.com/best-ollama-models-in-2025-complete-performance-comparison/)
- [Hugging Face GGUF Models](https://huggingface.co/models?library=gguf)
