from decimal import setcontext
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os,random
import calendar
import smtplib
email_dict = {'arpit':'arpitarora.bt19cse@pec.edu.in','mumma':'navjotkusum@gmail.com','naman':'nk.er13.6@gmail.com','papa':'harisharora67@gmail.com'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)  #here basically we have chosen a voice out of the voices which are avalaible in our computer.
def speak(audio_string):                #speak function takes input as audio in the form of a string.
    engine.say(audio_string)   
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. How may I help you")

def takeCommand():
    #It takes microphone input from user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1  #means while user is speaking, if user pauses in between for greater than 1sec, then it will stop listening, otherwise it will continue to listen.
        r.energy_threshold = 100
        audio = r.listen(source)   #basicallly what user speaks is saved in audio variable.

    try:
        print("Recognizing....")                                    
        query = r.recognize_google(audio , language="en-in")    # recognize_google performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Google Speech Recognition API.
        print(f"User said: {query}\n")                          #now we try to recognise using recognize_google what we have spoken by passing the audio variable to the 
                                                                #recognize_google function along with the language which is english-indian(en-in). It returns a string of what user has spoken.
                                                                #basically it converts audio(what user has spoken) into string.

    except Exception as e:                                      #we have used try except because there might be a case when google might not be able to recognize
        print("Say that again please...")                       #what the user has spoken. so if that is the case we ask the user to speak again.
        return "None"
    return query                                                #return the query string.
    

def sendEmail(recipient_email,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('assistantdesktop2324@gmail.com','arpit_2324')
    server.sendmail('assistantdesktop2324@gmail.com',recipient_email,content)
    server.close()

if __name__=="__main__":
   # wishMe()
    while True:
        query = takeCommand().lower() 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak('According to Wikipedia')
            speak(results)
        elif 'open youtube' in query:      #https://pythonexamples.org/python-open-url-in-chrome-browser/    ---> this is a useful link to study how to open any site in chrome browser using webrowser module in python.
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("youtube.com")
        elif 'open google' in query:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("stackoverflow.com")
        elif 'open whatsapp' in query:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("https://web.whatsapp.com/")
        elif 'open classroom' in query:
             webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
             webbrowser.get('chrome').open("https://classroom.google.com/u/1/h")
        elif 'open google meet' in query:
             webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
             webbrowser.get('chrome').open("https://meet.google.com/")
        elif 'open github' in query:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("https://github.com/")
        elif 'open linkedin' in query:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("https://www.linkedin.com/")
        elif 'quit' in query:
            exit()

        elif 'play music' in query:
            music_dir = "D:\\fav songs"   #if i want to play music ...first i will specify the directory in which my songs are present
            songs = os.listdir(music_dir)       #listdir basically makes a list of all the songs in the directory....this list is saved in a songs variable

            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))        #startfile basically khol dega hamari file ko and fir mein apni music_dir ko mila dunga
                                                                                             #or we can say join kar dunga songs[random no. between 0 and songs list ka size].....i have used
                                                                                             #random module so that a random no. is generated everytime and therefore a different song is played everytime.

            # os.startfile(os.path.join(music_dir,songs[0]))   ---> iss line ka matlab hai that it will play the first song in the songs list...as i have written songs[0]

        elif 'the time' in query:
            string_time  = datetime.datetime.now().strftime("%H:%M:%S")   #string_time contains the current time in the form of string
            speak(f"Sir the time is {string_time}")

        elif 'open vs code' in query:
            vs_path = "C:\\Users\\Arpit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"      #go to file location, then properties , then copy the target.
            os.startfile(vs_path)
        elif 'snake game' in query:
            game_path = "D:\\snake game_FINAL\\output\\main\\main.exe"
            os.startfile(game_path)
        elif 'send email' in query:
            try:
                speak('Please tell me the name of the recipient')
                recipient_name = takeCommand().lower()       #here we will take the input of the recipient name
                recipient_email = email_dict[recipient_name]          #here we will save the  recipient email in a variable using the email_dict.
                speak('what should I say')
                content = takeCommand()                    #here we take the input of the real email body.
                sendEmail(recipient_email,content)          #and then we call the send email function.
                speak("Email has been sent")
            except Exception as e:
                speak("Sorry! Email has not ben sent")          






