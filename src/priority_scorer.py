HIGH_PRIORITY_KEYWORDS = [
    "urgent",
    "deadline",
    "payment",
    "invoice",
    "exam",
    "assignment",
    "important",
    "immediately",
    "required"
]

MEDIUM_PRIORITY_KEYWORDS = [
    "meeting",
    "reminder",
    "project",
    "confirm",
    "schedule"
]


def calculate_priority(email: dict) -> str:
    """
    Calculates email priority using keyword-based scoring.
    """
    text = f"{email.get('subject', '')} {email.get('snippet', '')}".lower()

    for keyword in HIGH_PRIORITY_KEYWORDS:
        if keyword in text:
            return "High"

    for keyword in MEDIUM_PRIORITY_KEYWORDS:
        if keyword in text:
            return "Medium"

    return "Low"