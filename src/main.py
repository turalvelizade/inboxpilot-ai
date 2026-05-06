from agent import EmailTriageAgent


def main():
    """
    Entry point for InboxPilot AI.
    """
    print("InboxPilot AI - Gmail Email Triage Agent")
    print("Running Stage 2 sample email triage...")
    print()

    agent = EmailTriageAgent()
    report = agent.run_with_sample_data("data/sample_emails.json")

    print(report)


if __name__ == "__main__":
    main()