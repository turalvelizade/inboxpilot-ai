import os
import sys

sys.path.append(os.path.abspath("src"))

from ai_tool import classify_category, analyze_email_with_ai


def test_classify_finance_email():
    email = {
        "sender": "bank@example.com",
        "subject": "Payment confirmation",
        "snippet": "Please confirm your recent payment."
    }

    assert classify_category(email) == "Finance"


def test_classify_promotion_email():
    email = {
        "sender": "shop@example.com",
        "subject": "Discount offer",
        "snippet": "Get 40% off this weekend."
    }

    assert classify_category(email) == "Promotion"


def test_analyze_email_with_ai_returns_expected_fields(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    email = {
        "sender": "professor@example.com",
        "subject": "Assignment deadline",
        "snippet": "Submit your assignment before the deadline.",
        "date": "2026-05-10"
    }

    result = analyze_email_with_ai(email, "High")

    assert result["category"] == "University"
    assert result["priority"] == "High"
    assert "summary" in result
    assert "suggested_action" in result
    assert result["analysis_source"] == "local_fallback"