# Development Journal

## Step 1 – 24.04

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

```text
https://www.googleapis.com/auth/gmail.readonly
```

#### 2. Email Cleaner Tool

This tool will convert Gmail API responses into a simpler internal format. Gmail API responses can contain many technical fields, so the system will extract only the information needed for analysis.

The planned extracted fields are:

sender
subject
date
snippet or body preview

This makes the data easier to send to the AI model and easier to test.

#### 3. AI Triage Tool

This tool will send the cleaned email information to an external AI API, such as OpenRouter. The AI will analyze the email and return structured information.

The planned AI output fields are:

category
priority
summary
suggested action

Possible priority levels are:

High
Medium
Low

Possible categories are:

University
Work
Personal
Finance
Promotion
Newsletter
Spam
Other

#### 4. Priority Scoring Tool

This tool will help decide how important an email is. It may check for important words such as:

deadline
urgent
payment
invoice
meeting
assignment
exam
important

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

User runs the program from the command line.  
The program reads unread emails from Gmail.  
The user may choose how many emails to analyze.

The planned output is a triage report like this:

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

### Safety and Controlled Deployment Plan

The first version will use Gmail read-only access. This means the system cannot delete, archive, label, or send emails. This is important because the project uses real email data.

Sensitive files such as `.env`, `credentials.json`, and `token.json` will not be uploaded to GitHub. They will be listed in `.gitignore`.

The project will include clear setup instructions so another user can run it safely in a controlled environment.
