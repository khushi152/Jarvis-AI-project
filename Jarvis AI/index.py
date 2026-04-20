import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk




#dekho bs tumahre code me yahi galti thi ki tum na  voices = engine.getProperty('voices')   , engine.setProperty('voice',voices[0].id)
#engine.setProperty("rate",170)    ye tino ko function ke bahr likh rahe the right ab khud socho ye ek bar hi initialize ho raha tha aise smjhee 
#isliye ek bar bol raha tha jab dubara hum speak funtion call kar rahe the to ye initialize hi nahi hi raha tha isiye nhi bol raha tha 
#aur baki program kaam kar raha tha lekin bs bol nahi raha tha to hame lag raha tha kaam nhi kar rraha aur tum data ya time print bhi nahinkar rahe the smjheeee gawarrrrrr

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')      # getting details of current voice
    engine.setProperty('voice',voices[0].id)   #dekho ise uper ke line ko tum uper likh rahe the gawar function ke bahar aur socho jab ye initialize hi nahi hoga fir bolega kese is wo bs program start hote hi initialize hi raha tha ab duabra ho hi nahi raha tha initalize samjheee gawar
    engine.setProperty("rate",170)
    engine.say(audio)
    engine.runAndWait()


def command():
    content = ""
    while content == "":
        # obtain audio from the microphone
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
    # while True:
        # request = command().lower()
        request = command()
        request = request.lower().strip()
        
        # say hello
        if "hello"  in request:
            speak("Yes Boss ")

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
        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            print("Current time is "+ str(now_time)) # dekho tum print bhi nahi kar rahe the samjhe  isliye dikh nahi raha tha output aur hame kag raha tha kaam nahi kar raha lekin yr internally kaam kar raha tha bs bol  nahi rah tha 
            speak("Current time is "+ str(now_time))  #aur mai niche bhi sabhi function me print kar raha hu waha cokmment nahi likhunga

        #say date
        elif "say date" in request:
            now_time = datetime.datetime.now().strftime("%d:%m")
            print("Current date is "+ str(now_time))
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
        

        # for open google
        elif "open google" in request:
            request = request.replace("jarvis","")
            request = request.replace("search google","")
            webbrowser.open("https://www.google.com/search?q="+request)

        else :
            request = request.replace("jarvis","")
            request = request.replace("search wikipedia","")
            print(request)
            result = wikipedia.summary(request,sentences=2)
            print(result)
            speak(result)

    #ye dekho mene else case me wikipedia ke result ko rakh diya q ki jab uper ka koi command nahi chalega matlab sidhi si baat hogi tum 
    #search kar rahe task nahi kkarwa rahe to ye ekse case cahl jayega aur yahan se result de dega 
    #like samjho maximum extra question ka ans larega like mini chatgpt bs math ka chod ke wo bhi basic de hi dega shud
    #and congratulation tumne mini chatgpt bana liya 
        
speak("Initializing Jarvis ")        
while True:
   main_process()



#aur tumhara task ye hai ki ye bs bolne wlaa hai right to tum kya karna tum jab min_process ko call karo to wahan choice mile like
#1 dabao text chat ke liye aur 2 dabao aur voice ke liye smjhee its your task aur like exit wala kucch seen aisa ho ki 
# tum jab exit bolo to band ho jaye kaam na kare  ye loop me lagao smjhee baki khud karo 


#  aur maine kucch nahi kiyaa isme bs wo 2 ,3 line ko function ke andar dal diya aur bs print kiiya smjhee aur kuchh nahi 
#  baki sab tumne kiyaa hai smjhee