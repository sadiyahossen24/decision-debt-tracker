from openai import AzureOpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-01"
)

EXTRACTION_PROMPT = """
You are a Decision Extraction Agent. Analyze this meeting transcript and extract ALL decisions — both explicit and implicit.

For each decision extract:
- decision_text: Clear description of what was decided
- owner: Full name of responsible person ("Unassigned" if unclear)
- deadline: Specific date or timeframe ("None" if not mentioned)
- context: Why this decision was made (1-2 sentences)
- decision_type: One of [technical, financial, marketing, operational, hr]

Meeting: {meeting_title}
Date: {meeting_date}
Attendees: {attendees}

Transcript:
{transcript}

Return ONLY valid JSON array. No markdown, no explanation:
[{{"decision_text":"...","owner":"...","deadline":"...","context":"...","decision_type":"..."}}]
"""

def extract_decisions(transcript: str, meeting_title: str, meeting_date: str, attendees: str) -> list:
    prompt = EXTRACTION_PROMPT.format(
        meeting_title=meeting_title,
        meeting_date=meeting_date,
        attendees=attendees,
        transcript=transcript
    )
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    raw = response.choices[0].message.content
    raw = raw.replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        print(f"Parse error: {raw[:200]}")
        return []


