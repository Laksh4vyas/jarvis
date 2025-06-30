# 🎙️ AI Voice Assistant with Python

This is a simple yet smart **Voice Assistant** project built with Python that can greet you, search Google and Wikipedia, open websites, play music, tell the time/date, crack jokes, and more — all through **voice commands**. It also features a **Tkinter GUI animation window** that pops up when the assistant speaks.

---

## 🧠 Features

🎤 Voice-controlled interaction  
🧠 Wikipedia search and summaries  
🌐 Google and YouTube opener  
🎵 Play random local music files  
🕒 Tells current time and date  
😂 Speaks random jokes using `pyjokes`  
🗨️ Text-to-Speech using `pyttsx3`  
🖼️ Tkinter-based animated circle when speaking  
👂 Voice input with `speech_recognition`  

---

## 📁 Folder Structure

📦 voice-assistant/
├── assistant.py # Main application code
├── README.md # You're reading it :)


## 🛠️ Tech Stack

- **Programming Language**: Python 🐍
- **Libraries Used**:
  - `speech_recognition` – for voice input
  - `pyttsx3` – for text-to-speech
  - `wikipedia` – to fetch summaries
  - `webbrowser` – to open URLs
  - `os` – to access local files
  - `pyjokes` – for humor 😄
  - `tkinter` – to show a speaking animation

---

## 🚀 How to Run

### ✅ Step 1: Install dependencies

Install all the required libraries:

```bash
pip install pyttsx3 speechrecognition wikipedia pyjokes
✅ Tkinter comes pre-installed with Python.
✅ Webbrowser, os, random, datetime are built-in modules.

✅ Step 2: Update music path
In the code, update the following line with your local music folder:

python
Copy
Edit
music_dir = "C:\\Users\\Laksh\\Music"
Make sure it contains .mp3 files.

✅ Step 3: Run the assistant
bash
Copy
Edit
python assistant.py
Start speaking after the greeting. Try commands like:

"Search Python programming"

"Open YouTube"

"Tell me a joke"

"Play music"

"What time is it?"

"Tell me the date"

"Search Machine Learning on Wikipedia"

📌 Sample Voice Commands
Command	Action
"Open Google"	Opens Google in browser
"Search Python on Google"	Google search
"Wikipedia Artificial Intelligence"	Summary from Wikipedia
"Play music"	Plays a random MP3 file
"Tell me a joke"	Speaks a random joke
"What time is it"	Tells current time
"What is the date"	Tells today’s date
"Stop" or "Quit"	Exits the assistant

🧠 Improvements You Can Try
Add a GUI button to start voice command

Add user login

Save command history to a text file or DB

Add support for weather, news, or email reading

Integrate with ChatGPT API for smarter answers

👨‍💻 Author
Made with ❤️ by Laksh Vyas
📧 lakshvyas.dev@gmail.com

📜 License
This project is open-source and free to use under the MIT License.

yaml
Copy
Edit

---
