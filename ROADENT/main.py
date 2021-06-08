#from ROADENT.App.Voice_Commands import Voice_Commands
#from ROADENT.App.motors import *
#from ROADENT.App import *

#if __name__ == "__main__":

    #while True:
     #   Motor_1.clockwise()
     #   Voice_Commands()
import speech_recognition as sr

if __name__ == "__main__":
    r = sr.Recognizer()
    mic = sr.Microphone()
    sr.Microphone.list_microphone_names()
    mic = sr.Microphone(device_index=3)

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    x = r.recognize_google(audio)

    print(x)




