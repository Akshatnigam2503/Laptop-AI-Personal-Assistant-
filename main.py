import speech_recognition as sr
import webbrowser
import openai
import datetime
import os
import win32com.client
from config import apikey
from openai import OpenAI

chatStr = ""


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Akshat: {query}\n Jarvis: "
    client = OpenAI(api_key=apikey)

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response.choices[0].text)
    chatStr += f"{response.choices[0].text}\n"
    return response.choices[0].text


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    client = OpenAI(api_key=apikey)

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response.choices[0].text
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


def play_numbered_song():
    songs_inventory = [
    {"title": "On-and-On", "path": r"C:\Users\KIIT\Music\On-and-On_320(PaglaSongs).mp3"},
    {"title": "Positions", "path": r"C:\Users\KIIT\Music\Ariana_Grande_-_Positions.mp3"},
    {"title": "Tu Hai Kaun", "path": r"C:\Users\KIIT\Music\Tu_Hai_Kaun_Fotty_Seven.mp3"},
    {"title": "Chali Kahani", "path": r"C:\Users\KIIT\Music\Chali_Kahani.mp3"},
    {"title": "I don't miss that life", "path": r"C:\Users\KIIT\Music\i-dont-miss-that-life-seedhe-maut.mp4"},
]

    print("Available songs:")
    for i, song in enumerate(songs_inventory, start=1):
        print(f"{i}. {song['title']}")

    selected_song_number = int(input("Enter the number of the song you want to play: "))

    if 1 <= selected_song_number <= len(songs_inventory):
        selected_song = songs_inventory[selected_song_number - 1]
        os.system(f"start {selected_song['path']}")
        say(f"Playing {selected_song['title']}")
    else:
        print("Invalid selection. Please enter a valid song number.")


if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say(" Jarvis AI this side")
    while True:
        print("Listening...")
        query = takeCommand()

        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in query:
            play_numbered_song()

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} hours and {minute} minutes")

        elif "Using artificial intelligence" in query:
            ai(prompt=query)

        elif "Jarvis Quit" in query.lower():
            exit()

        elif "reset chat" in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
