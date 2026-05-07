# Development Journal

## Step 1

### Planned System Description and Goal

The planned system is called **InboxPilot AI: A Gmail-Based Email Triage Agent**.

The goal of the system is to help users manage unread emails more efficiently. Instead of opening every unread email manually, the user will run a Python command-line program. The system will connect to Gmail, read a limited number of unread emails, analyze their content, and return a structured triage report.

The report will show each email’s category, priority level, short summary, and suggested next action. The first version of the system will be read-only for safety. It will not delete, archive, send, or modify any emails.

### AI or Agent-Based Approach

The system will use a single intelligent agent called `EmailTriageAgent`.

The agent will control the workflow and decide which tool should be used at each step. The planned workflow is:

1. The user starts the command-line program.
2. The agent calls the Gmail Reader Tool to retrieve unread emails.
3. The agent calls the Email Cleaner Tool to extract and format important fields.
4. The agent sends the cleaned email data to an AI API.
5. The AI API returns a category, priority, summary, and suggested action.
6. The agent sends the analyzed results to the Report Generator Tool.
7. The final triage report is shown to the user.

This approach is agent-based because the program does not only perform one fixed function. The agent coordinates multiple tools and creates a meaningful result from external data.

### Planned Tools

The system will use the following tools:

#### 1. Gmail Reader Tool

This tool will connect to the Gmail API and retrieve unread emails from the user’s inbox. The planned Gmail permission is read-only, so the program can read messages but cannot modify them.

The planned Gmail scope is:

`https://www.googleapis.com/auth/gmail.readonly`

#### 2. Email Cleaner Tool

This tool will convert Gmail API responses into a simpler internal format. Gmail API responses can contain many technical fields, so the system will extract only the information needed for analysis.

The planned extracted fields are:

- sender
- subject
- date
- snippet or body preview

This makes the data easier to send to the AI model and easier to test.

#### 3. AI Triage Tool

This tool will send the cleaned email information to an external AI API, such as OpenRouter. The AI will analyze the email and return structured information.

The planned AI output fields are:

- category
- priority
- summary
- suggested action

Possible priority levels are:

- High
- Medium
- Low

Possible categories are:

- University
- Work
- Personal
- Finance
- Promotion
- Newsletter
- Spam
- Other

#### 4. Priority Scoring Tool

This tool will help decide how important an email is. It may check for important words such as:

- deadline
- urgent
- payment
- invoice
- meeting
- assignment
- exam
- important

The keyword result can support the AI classification and help the agent sort important emails first.

#### 5. Report Generator Tool

This tool will format the final output into a readable command-line report. The report will show the most important emails first and include the sender, subject, priority, category, summary, and suggested action.

### Preliminary Programming Concepts Required

The project will require the following programming concepts:

- Python functions
- Classes and objects
- Modules and imports
- Command-line input and output
- API integration
- OAuth authentication
- Environment variables
- JSON data processing
- Dictionaries and lists
- String cleaning and formatting
- Error handling
- Testing with pytest
- Git version control
- Documentation with README and journal files

### Planned Input and Output

The planned input is:

- User runs the program from the command line.
- The program reads unread emails from Gmail.
- The user may choose how many emails to analyze.

The planned output is a triage report like this:

```text
InboxPilot AI - Unread Email Triage Report

1. Priority: High
   Category: University
   From: professor@example.com
   Subject: Final project deadline
   Summary: The email reminds the student about an upcoming submission deadline.
   Suggested action: Read today and prepare a response.

2. Priority: Low
   Category: Promotion
   From: shop@example.com
   Subject: Weekend discount
   Summary: This is a marketing email about a sale.
   Suggested action: Ignore or archive later.
```

### Safety and Controlled Deployment Plan

The first version will use Gmail read-only access. This means the system cannot delete, archive, label, or send emails. This is important because the project uses real email data.

Sensitive files such as `.env`, `credentials.json`, and `token.json` will not be uploaded to GitHub. They will be listed in `.gitignore`.

The project will include clear setup instructions so another user can run it safely in a controlled environment.

---

## Step 2

### Updated System Description Based on Implementation Progress

The system has now moved from the planning phase into the implementation phase. The project has been developed as a structured Python command-line application with separate modules for the agent workflow, email cleaning, priority scoring, AI-style analysis, and report generation.

The current version uses sample email data from a local JSON file. This allows the workflow to be tested safely before connecting to a real Gmail inbox. The agent reads the sample emails, cleans the data, calculates priority, classifies the email category, generates a short summary, suggests an action, and displays a final triage report.

The system is still designed as a controlled and safe assistant. It does not delete, archive, send, or modify any real emails.

### Refined Programming Concepts Actually Used

The implementation uses the following programming concepts:

- Python functions for separate tool behavior
- A class for the main agent workflow
- Modules and imports for project organization
- File handling for loading sample email data
- JSON processing for structured email records
- Lists and dictionaries for storing and processing emails
- String processing for checking email content
- Conditional logic for category classification and priority scoring
- Error handling for missing files and invalid JSON
- Command-line output for displaying the final report
- Git version control for tracking implementation progress
- Documentation using README and journal files

### How These Concepts Are Applied in the Project

Functions are used to separate the responsibilities of each tool. The email cleaner tool prepares the raw email data, the priority scorer checks for important keywords, the AI-style triage tool classifies and summarizes each email, and the report generator formats the final output.

The `EmailTriageAgent` class coordinates the workflow. It loads the sample email data, calls the cleaner tool, calls the priority scorer, sends each email through the AI-style analysis tool, and then passes the results to the report generator.

JSON processing is used because email data can naturally be represented as structured records. Each email is stored as a dictionary with fields such as sender, subject, date, and snippet.

Error handling is included in the agent when loading the sample email file. If the file is missing or contains invalid JSON, the system returns an empty list and avoids crashing.

### Tool Integration

The tools are integrated through the `EmailTriageAgent`.

The current workflow is:

1. The agent loads sample emails from `data/sample_emails.json`.
2. The Email Cleaner Tool converts each email into a consistent format.
3. The Priority Scoring Tool checks the subject and snippet for important keywords.
4. The AI Triage Tool classifies the email category, creates a summary, and suggests an action.
5. The Report Generator Tool creates a readable command-line report.

This modular design makes the system easier to test, update, and extend. In the next version, the sample email loading tool can be replaced with a real Gmail API reader while keeping the rest of the workflow mostly unchanged.

### Current Implementation Progress

The current implementation includes:

- A working command-line entry point in `main.py`
- A main agent class in `agent.py`
- A sample email dataset in `data/sample_emails.json`
- An email cleaning module
- A priority scoring module
- An AI-style triage module
- A report generation module
- Error handling for file loading
- A readable triage report output

This version demonstrates the main agent workflow and tool integration before real Gmail and external AI API integration are added.
