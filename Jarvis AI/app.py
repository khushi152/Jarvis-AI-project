import streamlit as st
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import pywhatkit as pwk
from plyer import notification

# ---------- INIT ----------
engine = pyttsx3.init()
engine.setProperty("rate", 170)

# ---------- SPEAK ----------
def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------- VOICE INPUT ----------
def take_command():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.info("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        command = r.recognize_google(audio, language='en-in')
        return command.lower()

    except Exception:
        return "error"

# ---------- CORE LOGIC ----------
def process_command(request):
    response = ""

    if "hello" in request:
        response = "Hello! How can I help you?"

    elif "time" in request:
        now = datetime.datetime.now().strftime("%H:%M")
        response = f"Current time is {now}"

    elif "date" in request:
        now = datetime.datetime.now().strftime("%d %B %Y")
        response = f"Today's date is {now}"

    elif "open youtube" in request:
        webbrowser.open("https://youtube.com")
        response = "Opening YouTube"

    elif "open instagram" in request:
        webbrowser.open("https://instagram.com")
        response = "Opening Instagram"

    elif "search google" in request:
        query = request.replace("search google", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        response = f"Searching Google for {query}"

    elif "wikipedia" in request:
        query = request.replace("wikipedia", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            response = result
        except:
            response = "Sorry, I couldn't find anything"

    elif "send whatsapp" in request:
        pwk.sendwhatmsg("+91XXXXXXXXXX", "Hello from Jarvis", 22, 30)
        response = "Message scheduled"

    elif "show tasks" in request:
        try:
            with open("todo.txt", "r") as f:
                tasks = f.read()
            response = tasks
        except:
            response = "No tasks found"

    elif "add task" in request:
        task = request.replace("add task", "").strip()
        with open("todo.txt", "a") as f:
            f.write(task + "\n")
        response = f"Task added: {task}"

    elif "notify" in request:
        notification.notify(
            title="Reminder",
            message="Check your tasks!"
        )
        response = "Notification sent"

    elif "exit" in request:
        response = "Goodbye!"
        return response, True

    else:
        response = "Sorry, I didn't understand"

    speak(response)
    return response, False


# ---------- STREAMLIT UI ----------
st.set_page_config(page_title="AI Assistant 🤖", layout="centered")

st.title("🤖 AI Assistant (Jarvis UI)")
st.write("Voice + Text Controlled Assistant")

# Chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------- TEXT INPUT ----------
user_input = st.text_input("Type your command:")

col1, col2 = st.columns(2)

with col1:
    if st.button("Send"):
        if user_input:
            reply, exit_flag = process_command(user_input)
            st.session_state.chat.append(("You", user_input))
            st.session_state.chat.append(("Jarvis", reply))

with col2:
    if st.button("🎤 Speak"):
        voice = take_command()
        if voice != "error":
            reply, exit_flag = process_command(voice)
            st.session_state.chat.append(("You (voice)", voice))
            st.session_state.chat.append(("Jarvis", reply))
        else:
            st.error("Voice not recognized")

# ---------- DISPLAY CHAT ----------
st.subheader("Conversation")
for sender, msg in st.session_state.chat:
    if sender.startswith("You"):
        st.markdown(f"**🧑 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")