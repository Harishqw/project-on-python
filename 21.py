import pyttsx3
import speech_recognition as sr

def speak(audio):
    engine = pyttsx3.init()

    engine.say(audio)
    engine.runAndWait()

    
def take_commands():
    r=sr.recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("recongnizing")
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    return Query


# Driver Code
if __name__ == '__main__':
    # using while loop to communicate infinitely
    while True:
        command = take_commands()
        if "ID = 0" in command:
            Speak("order recive")
        if "ID = 1" in command:
            Speak("order recive")
        if "ID = 2" in command:
            Speak("order recive")
        if "ID = 3" in command:
            Speak("order recive")
        if "ID = 4" in command:
            Speak("order recive")
        if "ID = 5" in command:
            Speak("order recive")
        if "ID = 6" in command:
            Speak("order recive")
        else:
            Speak("thank you for your order")
        break
