import speech_recognition as sr   # its used for recognizing the voice.. convert voice to text    (https://realpython.com/python-speech-recognition/)
import pyttsx3                  # its used for convert text to voice .....    (https://www.devdungeon.com/content/text-speech-python-pyttsx3)
import smtplib                  # its used for sending mail.....     (https://docs.python.org/3/library/smtplib.html)
import datetime                 # its used for current date and time detection . its inbuilt module in python 3.7.
import webbrowser               # its used for connecrt with web..   (https://www.pythonforbeginners.com/code-snippets-source-code/python-webbrowser)
import wikipedia                # its used for wikipedia result .
import os                       # its used for Miscellaneous operating system interfaces    (https://docs.python.org/3/library/os.html)
engine = pyttsx3.init('sapi5')
                # sapi5 is a microsoft API
voices = engine.getProperty('voices')
            

engine.setProperty('voice',voices[1].id)
#engine.setProperty('voice',voices[0].id)
                # (voices[1] / voices[0]  is microsoft voice..its inbuilt in windows 10... in windows7, only one voice ,this is voice[0])




def speak(audio):    # speak(audio) is a function which is speak the text.
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    
    hour = int(datetime.datetime.now().hour)
            #int(datetime.datetime.now().hour) is current date,time format..
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")
    else:
      speak("Good Evening sir!")
      
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1 
                # listeining er por koto ta time por recognizing hba seta 'r.pause_threshold'  dia control kora jabe
        audio = r.listen(source)
    
        try:
            print("recognizing")
            query = r.recognize_google(audio, language='en-in')
                    
                      
            print(f"user said: {query}\n")
            
        except Exception as e:
            
            print("say that again sir..")
            return "None" 
        return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('csebinu@gmail.com', 'sukalyan1997')
            # server.login('sender_mail_ID@gmail.com', 'sender_mail_password')
    server.sendmail('csebinu@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    speak(" I am captain marvel.. Now you tell me How may I help you")
    #take_command()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.org")
        elif 'open python website' in query:
            webbrowser.open("python.org")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
                # here we add the website link for user query.
        elif 'email to marvel' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "	saugata97aeroxt@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")    

               