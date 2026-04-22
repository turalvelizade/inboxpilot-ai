# InboxPilot AI

InboxPilot AI is a planned Python command-line email triage agent.

The goal of the system is to connect to a Gmail inbox, read unread emails using the Gmail API, analyze them with an AI API, and return a structured triage report.

## Planned Features

- Read unread Gmail messages
- Extract sender, subject, date, and snippet
- Classify emails by priority
- Categorize emails
- Generate short summaries
- Suggest next actions
- Display a command-line report

## Safety

The first version will use Gmail read-only access. It will not delete, archive, send, or modify emails.

Sensitive files such as `.env`, `credentials.json`, and `token.json` must not be uploaded to GitHub.

## Current Status

Step 1: Planning and project structure.
