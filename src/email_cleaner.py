def clean_email(raw_email: dict) -> dict:
    """
    Converts raw email data into a clean internal format.
    Missing fields are replaced with default values.
    """
    return {
        "sender": raw_email.get("sender", "Unknown sender").strip(),
        "subject": raw_email.get("subject", "No subject").strip(),
        "date": raw_email.get("date", "Unknown date").strip(),
        "snippet": raw_email.get("snippet", "").strip()
    }


def clean_emails(raw_emails: list) -> list:
    """
    Cleans a list of raw email dictionaries.
    """
    return [clean_email(email) for email in raw_emails]