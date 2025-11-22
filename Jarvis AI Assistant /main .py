import speech_recognition as sr
import pyttsx3
import time
import re
import musicLibrary
import requests
import google.generativeai as genai
import textwrap


recognizer = sr.Recognizer()
ttsx = pyttsx3.init()


def speak(text):
    engine = pyttsx3.init(driverName='sapi5')  # force Windows speech engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # voices[1] if you want female
    engine.setProperty('rate', 175)
    print(f"[Jarvis Speaking]: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def AiProcess(command):
    import google.generativeai as genai
    import textwrap

    # Configure with your API key
    genai.configure(api_key="AIzaSyAdcBsyHQkN0K-up12njARk14PUK4WV8v4")

    # Choose the model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Generate content
    response = model.generate_content(command)

    # Get the text output
    output = response.text.strip()

    # Wrap text for neat alignment (80 chars per line)
    wrapped_output = textwrap.fill(output, width=80)

    # Print with a clean header and footer
    print("\n" + "="*40)
    print("🤖 Gemini Response")
    print("="*40 + "\n")
    print(wrapped_output)
    print("\n" + "="*40)
    return output


def processComand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        import webbrowser
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        import webbrowser
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        import webbrowser
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        import webbrowser
        webbrowser.open("https://www.instagram.com")

    elif "open linkedin" in c.lower():
        speak("Opening Linkedin")
        import webbrowser
        webbrowser.open("https://www.linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        import webbrowser
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=1fb6d0464e0149d781d455ef0f26e087")    
    

    else:
        output = AiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source)
                # recognizer.energy_threshold = 4000
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=8)

            # Convert speech to text
            command = recognizer.recognize_google(audio).lower()
            command = re.sub(r'[^a-z0-9 ]', '', command).strip()
            print("Heard:", command)

            # Wake word detection
            if "jarvis" in command:
                speak("Yes?")
                time.sleep(0.1)

                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio).lower()
                print("Command:", command)

                processComand(command)

        except sr.WaitTimeoutError:
            print("No speech detected, continuing...")

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
