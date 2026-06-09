## Decision Debt Radar

Organizations make decisions every week. Most never get implemented.
Decision Debt Radar is a multi-agent system built on Azure AI Foundry
that detects recurring unimplemented decisions and explains exactly why they fail.

## The Problem
Companies lose 70% of strategic decisions to poor follow-through.
Existing tools summarize meetings. No tool reasons about *why* decisions keep failing.

## What It Does
1. Extracts decisions from Teams meeting transcripts (GPT-4o)
2. Stores them in Foundry IQ knowledge base (Azure AI Search)
3. Detects recurring decisions using semantic retrieval + reasoning
4. Analyzes root causes (approval bottleneck, accountability gap, etc.)
5. Generates specific, assigned action items

## Microsoft Tools
- Azure AI Foundry — Agent orchestration
- Foundry IQ (Azure AI Search) — Grounded knowledge retrieval
- Azure OpenAI GPT-4o — Multi-step reasoning
- Azure OpenAI text-embedding-3-small — Semantic similarity
- GitHub Copilot — AI-assisted development

## Tech Stack
Python 3.11, FastAPI, Azure AI Foundry, Azure AI Search, Azure OpenAI, HTML/CSS/JS

## How to Run
1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and fill in Azure credentials
3. `python backend/foundry_iq/search_index.py`
4. `python process_all_meetings.py`
5. `python backend/main.py`
6. Open `frontend/index.html`

## Team
- [Piu] — Backend, Azure AI Foundry, Agents
- [Sadiya] — Frontend, Data, Demo



