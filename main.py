import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import webbrowser as wb

engine = pyttsx3.init() #object creation

engine.setProperty("rate", 150)#setting up new speaking rate
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)     #current volume level
engine.setProperty('volume',value=1) #printing current volume level

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) #voice[0] for male and voice[1] for female

#creating definitions for future importing from this main module
def talk(text):
    engine.say(text)
    engine.runAndWait()
def wishme():
    talk("hello brother welcome back i am your sister praveena ") #welcome text
    talk("What can i do for you")

def time():
    time = datetime.datetime.now().strftime('%I:%M %p') #time now in 12 hours format
    print(time)
    talk('current time is ' + time)
def date():
    today = datetime.datetime.now().strftime("today is " +"%d %B %Y") #todays date
    talk('current date is ' + today)
    print(today)

def take_command(): #function of speech recognition
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listenning...')
        listener.pause_threshold = 1
        voice = listener.listen(source)
    try:
        print("Recognizing....")
        command = listener.recognize_google(voice, language='en-in')
        print(command)
    except Exception as e:
        print(e)
        talk("Please say that again..")
        return "None"
    return command
#definition which will run if the main module is excuted
if __name__ =="__main__":
    wishme()
    while True:
        command = take_command().lower()

        if 'play' in command:
            video = command.replace('play','')
            talk('playing' +video)
            pywhatkit.playonyt(video)
        elif 'time' in command:
            time()
        elif 'date' in command:
            date()
        elif 'wikipedia' in command:
            talk("what should i search in wikipedia")
            data = take_command()
            talk("Searching...." + data)
            result = wikipedia.summary(data, sentences=2)
            print(result)
            talk(result)
        elif 'search in chrome' in command:
            talk("What should I search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = take_command().lower()
            wb.get(chromepath).open_new_tab(search)
        elif 'what is your name' in command:
            talk('My name is praveena')
        elif 'what is your mother name' in command:
            talk('My mother name is vennila')
        elif 'what is your brother name' in command:
            talk('My mother name is Gunasekaran')
        elif 'what is your brother name' in command:
            talk('My mother name is aravind')
        elif 'joke' in command:
            talk(pyjokes.get_joke())

        elif 'remember that' in command:
            talk("What should I remember?")
            data = take_command()
            talk("you said me to remember that " + data)
            remember = open('data.txt', 'w')
            remember.write(data)
        elif 'do you know anything' in command:
            remember = open('data.txt', 'r')
            talk("You said me to remember that" + remember.read())

        elif 'bye' in command:
            print("bye")
            talk("Bye")
            quit()
        else:
            take_command()
