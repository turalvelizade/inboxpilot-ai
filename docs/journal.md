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

---

## Step 3

### Testing Process

Testing was performed after the main implementation workflow was created. The project uses `pytest` to test the main tools and the full agent workflow. The testing process checks whether the system cleans email data correctly, calculates priority correctly, classifies emails correctly, handles empty input, and generates a readable triage report.

The tests use sample email dictionaries instead of real Gmail messages. This makes the tests safe and repeatable. It also avoids depending on internet access, real inbox data, or private user credentials.

The Gemini API integration includes a local fallback mode. If the API key is missing or the API request fails, the system can still analyze emails using local rule-based logic. This makes the software easier to test and safer for controlled deployment.

### Test Scenarios

#### Test Scenario 1: Email Cleaning with Complete Data

Input:

```text
sender: " professor@example.com "
subject: " Final deadline "
date: " 2026-05-10 "
snippet: " Submit your work. "
```

Expected result:

```text
sender: "professor@example.com"
subject: "Final deadline"
date: "2026-05-10"
snippet: "Submit your work."
```

Purpose:

This test verifies that the Email Cleaner Tool removes unnecessary spaces and returns a consistent email format.

#### Test Scenario 2: Email Cleaning with Missing Fields

Input:

```text
{}
```

Expected result:

```text
sender: "Unknown sender"
subject: "No subject"
date: "Unknown date"
snippet: ""
```

Purpose:

This test verifies that the system can handle incomplete email data without crashing.

#### Test Scenario 3: High Priority Detection

Input:

```text
subject: "Urgent payment required"
snippet: "Please confirm immediately."
```

Expected result:

```text
High
```

Purpose:

This test verifies that the Priority Scoring Tool detects urgent or important keywords.

#### Test Scenario 4: Medium Priority Detection

Input:

```text
subject: "Project meeting reminder"
snippet: "Please check the schedule."
```

Expected result:

```text
Medium
```

Purpose:

This test verifies that the Priority Scoring Tool can detect medium-priority emails.

#### Test Scenario 5: Low Priority Detection

Input:

```text
subject: "Weekend discount"
snippet: "Sale on selected items."
```

Expected result:

```text
Low
```

Purpose:

This test verifies that emails without important keywords are classified as low priority.

#### Test Scenario 6: Finance Category Classification

Input:

```text
sender: "bank@example.com"
subject: "Payment confirmation"
snippet: "Please confirm your recent payment."
```

Expected result:

```text
Finance
```

Purpose:

This test verifies that the AI triage tool can classify finance-related emails.

#### Test Scenario 7: Promotion Category Classification

Input:

```text
sender: "shop@example.com"
subject: "Discount offer"
snippet: "Get 40% off this weekend."
```

Expected result:

```text
Promotion
```

Purpose:

This test verifies that the AI triage tool can classify promotional emails.

#### Test Scenario 8: AI Tool Fallback Mode

Input:

```text
Email about assignment deadline with no GEMINI_API_KEY available.
```

Expected result:

```text
analysis_source: local_fallback
category: University
priority: High
```

Purpose:

This test verifies that the system still works when the Gemini API key is missing or unavailable.

#### Test Scenario 9: Full Agent Workflow

Input:

```text
sender: "professor@example.com"
subject: "Final project deadline reminder"
date: "2026-05-10"
snippet: "Please submit your final project before the deadline."
```

Expected result:

```text
The report contains:
- InboxPilot AI - Unread Email Triage Report
- Priority: High
- Category: University
```

Purpose:

This test verifies that the full agent workflow works correctly from raw email input to final report output.

#### Test Scenario 10: Empty Email List

Input:

```text
[]
```

Expected result:

```text
No emails found for triage.
```

Purpose:

This test verifies that the system handles empty input correctly.

### Testing Result

The tests were executed using the following command:

```bash
python -m pytest
```

The result was:

```text
11 passed
```

This confirms that the main tools and the complete agent workflow work correctly with the current sample-data implementation.

### Deployment Preparation

The project is prepared as a local command-line application. Another user can run it by cloning the GitHub repository, installing the dependencies, creating a local `.env` file, and running the main Python file.

The required dependencies are stored in `requirements.txt`.

To install dependencies:

```bash
python -m pip install -r requirements.txt
```

To run the current sample-data version:

```bash
python src/main.py
```

To run tests:

```bash
python -m pytest
```

The project includes `.env.example`, which explains the required environment variables. The real `.env` file must not be uploaded to GitHub because it contains private API keys.

Example `.env` file:

```env
GEMINI_API_KEY=your_real_gemini_api_key_here
USE_GEMINI=true
MAX_EMAILS=5
```

### Data Conversion and Porting

The current version uses sample email data stored in `data/sample_emails.json`.

The data conversion process is:

1. The agent loads raw email records from a JSON file.
2. Each raw email is represented as a Python dictionary.
3. The Email Cleaner Tool converts each dictionary into a consistent internal format.
4. The Priority Scoring Tool reads the cleaned subject and snippet.
5. The AI Triage Tool sends the cleaned email information to Gemini when an API key is available.
6. If Gemini is unavailable, the system uses local fallback logic.
7. The AI Triage Tool adds category, summary, priority, suggested action, and analysis source.
8. The Report Generator Tool converts the analyzed email dictionaries into a readable command-line report.

This process preserves correctness because every email is converted into the same structure before analysis.

### Deployment Strategy

The suitable deployment strategy for this project is a local command-line tool. This is appropriate because the system handles private email-related data and API keys. Running it locally gives the user more control over credentials and data.

A safe release strategy would be staged:

1. First release: sample-data version with tests.
2. Second release: Gemini API analysis with fallback mode.
3. Third release: Gmail API read-only inbox connection.
4. Future release: optional labels or archive suggestions, but only with user confirmation.

The first real inbox version should use Gmail read-only permission to reduce risk.
