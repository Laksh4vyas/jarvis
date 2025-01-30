import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import tkinter as tk
import time
import random

# Initialize the speech engine
engine = pyttsx3.init()

# Set properties of the speech engine (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 for male voice, 1 for female voice

# Function to create a tkinter window with a blue circle animation
def show_speaking_animation():
    """Displays a blue circle animation while the assistant is speaking."""
    window = tk.Tk()
    window.title("Voice Assistant")
    window.geometry("300x300")
    window.configure(bg='black')

    canvas = tk.Canvas(window, width=300, height=300, bg='black', highlightthickness=0)
    canvas.pack()

    # Draw a blue circle
    #canvas.create_oval(75, 75, 225, 225, fill='blue', outline='blue')
    #window.update()
    #time.sleep(2)

    # Destroy the window after the animation
    window.destroy()

# Function to convert text to speech
def speak(audio):
    """Converts text to speech and shows an animation."""
    show_speaking_animation()
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user based on the current time
def wishMe():
    """Greets the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, Laksh!")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Laksh!")
    else:
        speak("Good Evening, Laksh!")
    speak("I am your Assistant. How can I assist you today?")

# Function to take voice input from the user
def takeCommand():
    """Listens for a voice command and returns the recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
        except sr.WaitTimeoutError:
            speak("Listening timed out. Please try again.")
            return "None"
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat?")
            return "None"
        except Exception as e:
            print(f"Error: {str(e)}")
            return "None"

# Function to tell the current date
def tell_date():
    """Tells the current date."""
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today's date is {current_date}")

# Function to search Google
def google_search(query):
    """Searches Google for the given query."""
    search_query = query.replace("search", "").strip()
    speak(f"Searching Google for {search_query}")
    webbrowser.open(f"https://www.google.com/search?q={search_query}")

# Function to respond to voice commands
def respond_to_query(query):
    """Processes the user's command and performs corresponding actions."""

    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("The term is ambiguous. Please specify more clearly.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find any information on that topic.")

    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'search' in query:
        google_search(query)

    elif 'play music' in query:
        music_dir = "C:\\Users\\Laksh\\Music"  # Change this to your own music directory
        try:
            songs = [song for song in os.listdir(music_dir) if song.endswith('.mp3')]
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(music_dir, song))
                speak(f"Playing {song}")
            else:
                speak("No music files found in the directory.")
        except Exception as e:
            speak(f"An error occurred: {str(e)}")

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif 'date' in query:
        tell_date()

    elif 'joke' in query:
        speak(pyjokes.get_joke())

    elif 'stop' in query or 'quit' in query:
        speak("Goodbye, Laksh!")
        exit()

    else:
        speak("Sorry, I didn't understand that command. Please try again.")

# Main function
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if query and query != "None":
            respond_to_query(query)
