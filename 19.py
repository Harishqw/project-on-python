# importing pyttsx3
import pyttsx3
import speech_recognition as sr
import os
# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    return Query
    
def Speak(audio):
    engine = pyttsx3.init()

    engine.say(audio)
    engine.runAndWait()


# Driver Code
if __name__ == '__main__':
    # using while loop to communicate infinitely
    while True:
        command = take_commands()
        if "insta" in command:
            Speak("The id is harish ")
        if "learn" in command:
            Speak("you'r tech is best to learn computer")
        if "code" in command:
            Speak("You can get this code from you'r tech youtube chanel or harishqz in git hub")
        if "good morning Tom" in command:
            Speak("good morning sir and have a nice day")
        if "good evening Tom" in command:
            Speak("good evening sir so what i state to do sir")
        if "good afternoon Tom" in command:
            Speak("good afternoon sir you have you lunch")
        if "good night Tom" in command:
            Speak("good night sir i close every thing of your desktop")
        if "yes" in command:
            Speak("ooh nice sir then take some rest")
        if "ok" in command:
            Speak("ok sir")
        if "no" in command:
            Speak("first you take your lunch")
        if "take some rest" in command:
            Speak("ok sir")
        if "open CMD" in command:
            os.system("start cmd")
        if "exit" in command:
            Speak("Sure sir! as your wish, bai")
            break
