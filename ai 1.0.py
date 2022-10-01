# importing pyttsx3
import pyttsx3
import speech_recognition as sr
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
        if "hello" in command:
            speak(" hlo sir i am jarvis how may i help you")
            break
        if "exit" in command:
            Speak("Sure sir! as your wish, bai")
            break
        if "insta" in command:
            Speak("The id is harish ")
        if "learn" in command:
            Speak("you'r tech is best to learn computer")
            break
        if "code" in command:
            Speak("You can get this code from you'r tech youtube chanel or harishqz in git hub")
            break
        if "open google" in command:
            speak(" hlo sir i am jarvis how may i help you")
            break
        if "open notepad" in command:
            speak(" hlo sir i am jarvis how may i help you")
            break
        if "good morning" in command:
            speak(" good morning sir and have a nice day")
            break
        if "good evening" in command:
            speak("good evening sir you have your lunch")
            break
        if "yes" in command:
            speak("ooh nice sir")
            break
        if "no" in command:
            speak("why sir why you not take your lunch")
            break
        if "thanks" in command:
            speak("ooh sir it's my plesur")
            break
        if "good afternoon" in command:
            speak(" good afternoon sir shal we start a new project ")
            break
        if "teak a few minute " in command:
            speak("ok sir")
            break
        if "good night" in command:
            speak("how was your today's day sir")
            break
        if "nice" in command:
            speak("ooh good ok sir good night exit")
            break
        if "time" in command:
            speak("it's your good time")
            break
