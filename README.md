# Virtual-Assistant



## Overview

This is a simple voice assistant script written in Python that utilizes various libraries to perform tasks such as setting reminders, creating to-do lists, searching the web, and providing help commands.

## Features

### 1. Set Reminders

You can instruct the voice assistant to set reminders by saying phrases like "set a reminder for [event] at [time]." The assistant will then prompt you for the event details and the time to set the reminder.

### 2. Create To-Do Lists

You can create to-do lists by saying "create a to-do list." The assistant will guide you through adding tasks one by one, and when you're finished, it will read back the entire to-do list.

### 3. Search the Web

Searching the web is possible by saying "search for [query]." The assistant will then open a web browser and perform a Google search with the provided query.

### 4. Show Available Commands (Help)

To get a list of available commands, you can say "help." The assistant will provide a summary of tasks it can perform.

### 5. Exit

To exit the voice assistant, you can say "exit" or "quit." The assistant will bid you goodbye.

## Dependencies

The script relies on the following Python libraries:

- `os`: Operating system-specific functionality.
- `datetime`: Date and time-related operations.
- `webbrowser`: Opening and displaying web-based documents.
- `speech_recognition`: Recognizing speech input.
- `gtts` (Google Text-to-Speech): Converting text to speech and saving it as an audio file.
- `sounddevice` and `numpy`: Handling audio input and output.
- `playsound`: Playing sound files.

## Getting Started

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the script with `python voice_assistant.py`.
4. Interact with the voice assistant by speaking the supported commands.

## Usage Examples

- **Setting a Reminder:**
  ```
  User: Set a reminder for a meeting at 3:00 PM.
  Assistant: What should I remind you about?
  User: Team meeting.
  Assistant: When do you want to be reminded? Please say the time in hours and minutes.
  User: 3 00
  Assistant: Alright, I will remind you about 'Team meeting' at 03:00 PM.
  ```

- **Creating a To-Do List:**
  ```
  User: Create a to-do list.
  Assistant: Let's create a to-do list. Please say the tasks one by one. Say 'done' when you're finished.
  User: Buy groceries.
  Assistant: Added: Buy groceries.
  User: Complete project report.
  Assistant: Added: Complete project report.
  User: Done.
  Assistant: Here's your to-do list:
           Buy groceries.
           Complete project report.
  ```

- **Searching the Web:**
  ```
  User: Search for Python tutorials.
  Assistant: Searching for 'Python tutorials.'
  ```

