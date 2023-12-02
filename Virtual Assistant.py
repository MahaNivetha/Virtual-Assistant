#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import datetime
import webbrowser
import speech_recognition as sr
from gtts import gTTS
import sounddevice as sd
import numpy as np
import playsound

def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("output.mp3")
    playsound.playsound("output.mp3")
    os.remove("output.mp3")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(f"User said: {command}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"

    return command.lower()

def set_reminder(command):
    speak("What should I remind you about?")
    reminder = listen()
    speak("When do you want to be reminded? Please say the time in hours and minutes.")
    reminder_time = listen()
    try:
        hour, minute = map(int, reminder_time.split())
        now = datetime.datetime.now()
        reminder_datetime = now.replace(hour=hour, minute=minute)
        if now > reminder_datetime:
            reminder_datetime += datetime.timedelta(days=1)
        speak(f"Alright, I will remind you about '{reminder}' at {hour:02d}:{minute:02d}.")
        while True:
            if datetime.datetime.now() >= reminder_datetime:
                speak(f"Reminder: {reminder}")
                break
    except ValueError:
        speak("Sorry, I couldn't understand the time you provided. Please try again.")

def create_todo_list(command):
    todo_list = []
    speak("Let's create a to-do list. Please say the tasks one by one. Say 'done' when you're finished.")
    while True:
        task = listen()
        if task == "done":
            break
        todo_list.append(task)
        speak(f"Added: {task}")
    speak("Here's your to-do list:")
    for task in todo_list:
        speak(task)

def search_web(command):
    search_terms = command.replace("search", "").strip()
    if search_terms:
        url = f"https://www.google.com/search?q={search_terms}"
        speak(f"Searching for '{search_terms}'")
        webbrowser.open(url)
    else:
        speak("Please provide a search term.")

def show_help():
    help_text = """
    I can help you with the following tasks:
    1. Set reminders: Say 'set reminder' followed by the reminder and time.
    2. Create to-do lists: Say 'create to-do list' and then list your tasks one by one.
    3. Search the web: Say 'search' followed by the search terms.
    4. Show available commands: Say 'help'.
    5. To exit, say 'exit' or 'quit'.
    """
    print(help_text)
    speak(help_text)

def main():
    speak("Hello , I am your voice assistant. How can I help you today?")
    
    while True:
        command = listen()
        
        if "reminder" in command:
            set_reminder(command)
        elif "to-do" in command or "todo" in command:
            create_todo_list(command)
        elif "search" in command:
            search_web(command)
        elif "help" in command:
            show_help()
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that. Please try again.")
            continue

if __name__ == "__main__":
    main()


# In[ ]:




