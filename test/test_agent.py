import os
import sys

sys.path.append(os.path.abspath("src"))

from agent import EmailTriageAgent


def test_agent_triage_emails_generates_report(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    agent = EmailTriageAgent()

    raw_emails = [
        {
            "sender": "professor@example.com",
            "subject": "Final project deadline reminder",
            "date": "2026-05-10",
            "snippet": "Please submit your final project before the deadline."
        }
    ]

    report = agent.triage_emails(raw_emails)

    assert "InboxPilot AI - Unread Email Triage Report" in report
    assert "Priority: High" in report
    assert "Category: University" in report


def test_agent_handles_empty_email_list():
    agent = EmailTriageAgent()

    report = agent.triage_emails([])

    assert report == "No emails found for triage."