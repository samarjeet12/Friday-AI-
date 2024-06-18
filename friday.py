import os 

try:
    import speech_recognition as sr
except:
    os.system("pip install speechrecognition")
    import speech_recognition as sr


try:
    import datetime
except:
    os.system("pip install datetime")
    import datetime


try:
    import pyttsx3
except:
    os.system("pip install pyttsx3")
    import pyttsx3


try:
    import wikipedia
except:
    os.system("pip install wikipedia")
    import wikipedia


try:
    import pyjokes
except:
    os.system("pip install pyjokes")
    import pyjokes


try:
    import pywhatkit as kit
except:
    os.system("pip install pywhatkit")
    import pywhatkit as kit


try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui


try:
    import webbrowser
except:
    os.system("pip install webbrowser")
    import webbrowser


try:
    from AppOpener import open, close
except:
    os.system("pip install appopener")
    from AppOpener import open, close


try:
    import subprocess
except:
    os.system("pip install subprocess")
    import subprocess


try:
    import time
except:
    os.system("pip install time")
    import time

try:
    from googletrans import Translator
except:
    os.system("pip install string")
    from googletrans import Translator


try:
    import google.generativeai as palm
except:
    os.system("pip install google-generativeai")
    import google.generativeai as palm

try:
    import tkinter as tk
except:
    os.system("pip install tk")
    import tkinter as tk

try: 
    from PIL import Image, ImageTk
except:
    os.system("pip install pillow")
    from PIL import Image, ImageTk


print("Initializing.......")
print("Setting Properties...")


API_KEY = "AIzaSyBnWc8zQQqtYwi-60Ubo_ZUuOJGwEaWZcI"

def say(text, rate=170):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', rate)
    print("")
    print("")
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say(f"Good Morning Boss.")

    elif hour >= 12 and hour < 18:
        say(f"Good Afternoon Boss.")

    else:
        say(f"Good Evening Boss.")


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)  
        audio_data = recognizer.listen(source)      
        
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio_data)  
            text = str(text).lower()
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return ""
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))
            return ""


def translate_hindi_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='hi', dest='en')
    return translation.text


def main():
    try:
        hindi_text = listen()
        english_translation = translate_hindi_to_english(hindi_text)
        english_translation = english_translation.lower()
        print("English Translation:", english_translation)
        return english_translation
    except: 
        return ""


if __name__ == '__main__':
    wishMe()
    process_video = subprocess.Popen(["python", "video.py"])

    while True:

        query = main()

        if "open youtube" in query:
            webbrowser.open("https://www.youtube.com")

        elif query == '':
            pass

        elif "open" in query:
            app_name = query.replace("open ","")
            open(app_name, match_closest=True)

        elif "close " in query:
          app_name = query.replace("close ","").strip()
          close(app_name, match_closest=True, output=False)

        elif 'sleep friday' in query or 'bye friday' in query:
            print("Exiting.....")
            say("bye boss")
            break
            
        elif "what you can do" in query :
            print("i can open and close apps, perform search on web, solving your problems, give advises, search products on amazon, playing videos on youtube")

        elif "who are you" in query or "introduce yourself" in query or 'Tell me about yourself' in query:
            print(f"Hello, I'm Friday, your next-gen AI desktop assistant. With a sleek interface and a myriad of skills, I'm here to streamline your digital life. From opening and closing apps to cracking jokes and answering your burning questions, I've got you covered. Whether you need to search on Amazon, delve into Wikipedia, or simply unwind with YouTube videos, I'm your go-to companion. So, let's make every day a breeze together.")
            say(f"Hello, I'm Friday, your next-gen AI desktop assistant. With a sleek interface and a myriad of skills, I'm here to streamline your digital life. From opening and closing apps to cracking jokes and answering your burning questions, I've got you covered. Whether you need to search on Amazon, delve into Wikipedia, or simply unwind with YouTube videos, I'm your go-to companion. So, let's make every day a breeze together.")

        elif "search on amazon" in query:
            message = query.replace("search on amazon ", "")
            message = str(message)
            url = 'https://www.amazon.in/s?k=' + message 
            webbrowser.open(url)

        elif "joke" in query:
            say(pyjokes.get_jokes())

        elif "according to wikipedia" in query:
            try:
                query = query.replace("friday","")
                print("Searching......")
                print(wikipedia.summary(query, sentences=2))
                say(wikipedia.summary(query, sentences=2))
            except:
                print("can't find your query on wikipedia")
                say("can't find your query on wikipedia")

        elif "search on Google" in query:
            print("Searching......")
            kit.search(query)

        elif "play on youtube" in query:
            say("what should i play on youtube")
            video_query = listen()
            kit.playonyt(video_query)

        elif "tell the time" in query or "whats the time" in query:
            time = str(datetime.datetime.now())
            hour = time[11:13]
            min = time[14:16]
            say("The time is " + hour + " Hours and " + min + " Minutes ")

        elif "switch tab" in query or "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        else:
            try:
                palm.configure(api_key= API_KEY)
                message = query
                response = palm.chat(context="human", messages = message)
                print("Thinking...😒")
                if (response.last !=None):
                    print(f" J.A.R.V.I.S : {response.last}")
                    say(response.last)

                if (response.last==None):
                    palm.configure(api_key=API_KEY)
                    prompt = query
                    print('Generating...')
                    completion = palm.generate_text(
                        model='models/text-bison-001',
                        prompt=prompt,
                        temperature=1,
                        max_output_tokens=200,
                    )

                    if (completion.result==None):
                        print("I Dont have real time data so i cant answer this question")
                        say("I Dont have real time data so i cant answer this question")
                    else:
                        print(completion.result)

            except Exception as e:
                say("i can't answer this question")
            
            
         
    

        
