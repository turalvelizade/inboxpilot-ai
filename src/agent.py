import json

from email_cleaner import clean_emails
from priority_scorer import calculate_priority
from ai_tool import analyze_email_with_ai
from report_generator import generate_report


class EmailTriageAgent:
    """
    Main agent that coordinates the email triage workflow.
    """

    def load_sample_emails(self, file_path: str) -> list:
        """
        Loads sample emails from a local JSON file.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: Sample email file was not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Sample email file is not valid JSON.")
            return []

    def triage_emails(self, raw_emails: list) -> str:
        """
        Runs the full triage workflow.
        """
        cleaned_emails = clean_emails(raw_emails)
        analyzed_emails = []

        for email in cleaned_emails:
            priority = calculate_priority(email)
            ai_result = analyze_email_with_ai(email, priority)

            analyzed_email = {
                **email,
                **ai_result
            }

            analyzed_emails.append(analyzed_email)

        return generate_report(analyzed_emails)

    def run_with_sample_data(self, file_path: str) -> str:
        """
        Runs the agent using local sample email data.
        """
        raw_emails = self.load_sample_emails(file_path)
        return self.triage_emails(raw_emails)