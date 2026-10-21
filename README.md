# Python for AI - Module 1

Small Python programs from Module 1 (Python Basics for GenAI and Agentic AI).

## Task 1.8: City Care Bot (design)

**Business:** City Care Clinic. The staff answer the same questions all day, so this bot handles the common ones, hands complaints to a human, and counts the questions it could not answer.

File: `code/lesson_08_mini_chatbot.py`. Run it with `uv run code/lesson_08_mini_chatbot.py`.

### Intent table

The bot checks the rows from top to bottom and uses the first one that matches.

| # | Intent (what the user wants) | Keywords to look for | Reply |
|---|---|---|---|
| 1 | Talk to a human (handover) | `human`, `agent` | Connecting you to a human... (chat ends) |
| 2 | Complaint | `complain`, `problem`, `rude`, `is late`, `delay` | Sorry about that. The clinic manager will call you today. |
| 3 | Say goodbye | `bye` (exact match) | Take care, {name}! (chat ends) |
| 4 | Greeting | `hi`, `hello` (exact match), starts with `hey` | Hello {name}! How can I help you? |
| 5 | Timings | `timing`, `open`, `hours`, `what time` | We are open 10 am to 8 pm, Monday to Saturday. |
| 6 | Fees | `fee`, `price`, `cost`, `how much` | Consultation fee is 2,000 PKR. |
| 7 | Location | `where`, `location`, `address` | We are on Main Boulevard, near City Mall. |
| 8 | Appointments | `appointment`, `book` | To book an appointment, please call our front desk. |
| 9 | Thanks | `thank` | You're welcome, {name}! |
| 10 | Anything else (fallback) | no keyword matched | Counts as unanswered and prints the AI prompt for Module 2. |

### Design decisions

- The complaint and human rules come first, so an upset customer never gets a normal answer.
- Short words like `hi` use `==` or `.startswith()`, because `"hi" in "which"` is `True`.
- Every message is cleaned with `.strip().lower()` before any check.
- When the user types `bye` (or asks for a human), the bot prints a summary of messages, unanswered questions and complaints.
