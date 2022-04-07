import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import wolframalpha
import requests
import pyjokes


print('Loading your assistant - AeOne')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)



def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your assistant Aeone")



if __name__=='__main__':


    while True:
        speak("Tell me, how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if  "ok bye" in statement or "stop" in statement:
            speak(' assistant Aeone is shutting down,bye')
            print(' assistant Aeone is shutting down, bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement,3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            
            break

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            
            break

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            
            break

        elif 'how are you' in statement :
            speak("I m fine, Thankyou.")
            speak("and how are you ?")

        elif 'fine' in statement:
            speak("glad to know that you are fine, make sure you wear mask when go out")
            time.sleep(4)    


        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am aeone, your assistant. I can do minor tasks like opening google, youtube, mail, answer your questions and you can ask me computational and geographical questions too')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Vanshika yadav")
            print("I was built by Vanshika yadav")

        elif "joke" in statement:
            speak(pyjokes.get_joke())    



        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(3)
            break

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            

time.sleep(3)

                

