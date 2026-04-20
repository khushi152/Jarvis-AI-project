import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')       # getting details of current voice
    engine.setProperty('voice',voices[0].id)
    engine.setProperty("rate",170)
    engine.say(audio)
    engine.runAndWait()

def command():
    content = ""
    while content == "":
        # # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            r.adjust_for_ambient_noise(source,duration=1)
            audio = r.listen(source)

        try:
            content =r.recognize_google(audio , language='en-in')
            print("You Said......." + content)
        except Exception as e:
            print("Please try again...")    
    return content 

def main_process():
    while True:
        request = command().lower()
        # say hello
        if "hello" in request:
            speak("Welcome,How can i help you.")

        # say play music
        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1,3)
            if song ==1:
                webbrowser.open("https://www.youtube.com/watch?v=rSxTumD4kew&list=RDrSxTumD4kew&start_radio=1")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=-2RAq5o5pwc&list=RD-2RAq5o5pwc&start_radio=1")
            elif song == 3:
               webbrowser.open("https://www.youtube.com/watch?v=udgrClXV26Y&list=RDudgrClXV26Y&start_radio=1")

        # say time
        elif "time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            print("Current time is "+ str(now_time))
            speak("Current time is "+ str(now_time))


        #say date
        elif "date" in request:
            now_time = datetime.datetime.now().strftime("%d:%m")
            print("Current time is "+ str(now_time))
            speak("Current date is "+ str(now_time))

        # say new task he will note your task
        elif "new task" in request:
            task = request.replace("new task","")
            task = task.strip()
            if task !="":
                speak("Adding task : "+ task)
                with open ("todo.txt", "a") as file:
                    file.write(task + "\n")

        # say speak atsk he will speak all task
        elif "speak task" in request:
            with open ("todo.txt","r")  as file:
                speak ("Work we have to do today is :" + file.read()) 

        # for show notification of task
        elif "show work" in request:
            with open ("todo.txt","r") as file:
                task= file.read()
            notification.notify(
                title ="Today's work ",
                message = task
            )

        # delete task
        elif "delete task" in request:
            task = request .replace("delete task","")
            task = task.strip()
            with open ("todo.txt","r") as file:
                tasks = file . readlines()
            with open("todo.txt","w") as file:
                for t in tasks:
                    if task not in t:
                        file.write(t)
            speak("Task deleted successfully")

        # FOR OPEN  any website
        elif "open youtube " in request:
            webbrowser.open("https://www.youtube.com")
        elif "open insta" in request:
            webbrowser.open("https://www.instagram.com")


        # for open any application 
        elif "open" in request :
            query = request.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query) 
            pyautogui.sleep(2)
            pyautogui.press("enter")

        # response from wikipedia say jarvis search wikipedia about.....
        elif "wikipedia" in request:
            request = request.replace("jarvis","")
            request = request.replace("search wikipedia","")
            print(request)
            result = wikipedia.summary(request,sentences=2)
            print(result)
            speak(result)

        # for open google
        elif "search google" in request:
            request = request.replace("jarvis","")
            request = request.replace("search google","")
            webbrowser.open("https://www.google.com/search?q="+request)

        # SEND  whatsapp msg
        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+61404681324","hi, how are you",22,49,15)
speak("initializing jarvis")      
main_process()
