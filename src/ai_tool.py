def classify_category(email: dict) -> str:
    """
    Classifies email category using simple AI-like rules.
    Later this can be replaced with an external AI API.
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
    Generates a short summary from the email subject and snippet.
    """
    subject = email.get("subject", "No subject")
    snippet = email.get("snippet", "")

    if len(snippet) > 120:
        snippet = snippet[:120] + "..."

    return f"The email is about: {subject}. {snippet}"


def suggest_action(priority: str, category: str) -> str:
    """
    Suggests a next action based on priority and category.
    """
    if priority == "High":
        return "Read and respond as soon as possible."

    if category == "Promotion":
        return "Ignore unless you are interested."

    if priority == "Medium":
        return "Review when you have time."

    return "No immediate action needed."


def analyze_email_with_ai(email: dict, priority: str) -> dict:
    """
    Simulates AI triage output for one email.
    """
    category = classify_category(email)

    return {
        "category": category,
        "priority": priority,
        "summary": generate_summary(email),
        "suggested_action": suggest_action(priority, category)
    }