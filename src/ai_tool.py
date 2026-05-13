import json
import os

from dotenv import load_dotenv

load_dotenv()


def classify_category(email: dict) -> str:
    """
    Fallback category classifier using simple rules.
    Used when Gemini API is unavailable or returns invalid output.
    """
    text = f"{email.get('sender', '')} {email.get('subject', '')} {email.get('snippet', '')}".lower()

    if "payment" in text or "bank" in text or "invoice" in text:
        return "Finance"

    if "discount" in text or "offer" in text or "sale" in text or "shop" in text:
        return "Promotion"

    if "professor" in text or "assignment" in text or "exam" in text or "deadline" in text:
        return "University"

    if "meeting" in text or "work" in text:
        return "Work"

    return "Other"


def generate_summary(email: dict) -> str:
    """
    Fallback summary generator.
    """
    subject = email.get("subject", "No subject")
    snippet = email.get("snippet", "")

    if len(snippet) > 120:
        snippet = snippet[:120] + "..."

    return f"The email is about: {subject}. {snippet}"


def suggest_action(priority: str, category: str) -> str:
    """
    Fallback action suggestion.
    """
    if priority == "High":
        return "Read and respond as soon as possible."

    if category == "Promotion":
        return "Ignore unless you are interested."

    if priority == "Medium":
        return "Review when you have time."

    return "No immediate action needed."


def fallback_analysis(email: dict, priority: str) -> dict:
    """
    Returns local rule-based analysis if Gemini is unavailable.
    """
    category = classify_category(email)

    return {
        "category": category,
        "priority": priority,
        "summary": generate_summary(email),
        "suggested_action": suggest_action(priority, category),
        "analysis_source": "local_fallback"
    }


def analyze_email_with_gemini(email: dict, priority: str) -> dict:
    """
    Uses Gemini API to analyze one email.
    If the API key is missing or the API fails, local fallback analysis is used.
    """
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return fallback_analysis(email, priority)

    try:
        from google import genai

        client = genai.Client(api_key=api_key)

        prompt = f"""
You are an email triage assistant.

Analyze this email and return ONLY valid JSON.
Do not include markdown.

Email:
Sender: {email.get("sender", "")}
Subject: {email.get("subject", "")}
Date: {email.get("date", "")}
Snippet: {email.get("snippet", "")}

Priority already calculated by local tool: {priority}

Return JSON with exactly these fields:
category, priority, summary, suggested_action

Allowed categories:
University, Work, Personal, Finance, Promotion, Newsletter, Spam, Other

Allowed priority values:
High, Medium, Low
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        data = json.loads(response.text)

        return {
            "category": data.get("category", "Other"),
            "priority": data.get("priority", priority),
            "summary": data.get("summary", generate_summary(email)),
            "suggested_action": data.get(
                "suggested_action",
                suggest_action(priority, data.get("category", "Other"))
            ),
            "analysis_source": "gemini_api"
        }

    except Exception:
        return fallback_analysis(email, priority)


def analyze_email_with_ai(email: dict, priority: str) -> dict:
    """
    Main AI analysis function used by the agent.
    """
    return analyze_email_with_gemini(email, priority)