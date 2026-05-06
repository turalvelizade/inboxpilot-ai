def generate_report(analyzed_emails: list) -> str:
    """
    Creates a readable command-line triage report.
    """
    if not analyzed_emails:
        return "No emails found for triage."

    priority_order = {"High": 1, "Medium": 2, "Low": 3}

    sorted_emails = sorted(
        analyzed_emails,
        key=lambda email: priority_order.get(email.get("priority", "Low"), 3)
    )

    report_lines = []
    report_lines.append("InboxPilot AI - Unread Email Triage Report")
    report_lines.append(f"Emails analyzed: {len(sorted_emails)}")
    report_lines.append("")

    for index, email in enumerate(sorted_emails, start=1):
        report_lines.append(f"{index}. Priority: {email['priority']}")
        report_lines.append(f"   Category: {email['category']}")
        report_lines.append(f"   From: {email['sender']}")
        report_lines.append(f"   Subject: {email['subject']}")
        report_lines.append(f"   Date: {email['date']}")
        report_lines.append(f"   Summary: {email['summary']}")
        report_lines.append(f"   Suggested action: {email['suggested_action']}")
        report_lines.append("")

    return "\n".join(report_lines)