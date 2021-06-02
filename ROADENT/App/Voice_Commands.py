import speech_recognition as sr
from ROADENT.App import *


def Voice_Commands():

    r = sr.Recognizer()
    mic = sr.Microphone()
    # sr.Microphone.list_microphone_names()
    mic = sr.Microphone(device_index=3)

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    x = r.recognize_google(audio)

    if x == 'go':
        Motor_1.clockwise(5)
        Motor_2.c_clockwise(5)
    elif x == 'stop':
        Motor_1.STOP()
        Motor_2.STOP()
    elif x == 'left':
        Motor_1.clockwise(5)
        Motor_2.clockwise(5)
    elif x == 'right':
        Motor_1.c_clockwise(5)
        Motor_2.clockwise(5)