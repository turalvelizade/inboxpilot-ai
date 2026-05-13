import os
import sys

sys.path.append(os.path.abspath("src"))

from email_cleaner import clean_email, clean_emails


def test_clean_email_with_all_fields():
    raw_email = {
        "sender": " professor@example.com ",
        "subject": " Final deadline ",
        "date": " 2026-05-10 ",
        "snippet": " Submit your work. "
    }

    cleaned = clean_email(raw_email)

    assert cleaned["sender"] == "professor@example.com"
    assert cleaned["subject"] == "Final deadline"
    assert cleaned["date"] == "2026-05-10"
    assert cleaned["snippet"] == "Submit your work."


def test_clean_email_with_missing_fields():
    cleaned = clean_email({})

    assert cleaned["sender"] == "Unknown sender"
    assert cleaned["subject"] == "No subject"
    assert cleaned["date"] == "Unknown date"
    assert cleaned["snippet"] == ""


def test_clean_emails_list():
    raw_emails = [
        {"sender": "a@example.com", "subject": "Hello"},
        {"sender": "b@example.com", "subject": "Test"}
    ]

    cleaned = clean_emails(raw_emails)

    assert len(cleaned) == 2
    assert cleaned[0]["sender"] == "a@example.com"
    assert cleaned[1]["sender"] == "b@example.com"