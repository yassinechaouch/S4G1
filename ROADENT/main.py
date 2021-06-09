from App import *

#if __name__ == "__main__":

    #while True:
     #   Motor_1.clockwise()
     #   Voice_Commands()
import speech_recognition as sr

if __name__ == "__main__":
    r = sr.Recognizer()
    r.energy_threshold = 5000
    mic = sr.Microphone(device_index=1)
    print(sr.Microphone.list_microphone_names())

    with mic as source:
        print("Say now!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 3)

    my_string = r.recognize_google(audio)
    print(my_string)
