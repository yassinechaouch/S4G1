'''import speech_recognition as sr
from ROADENT.App import *


def voice_commands():

    # SENSOR1.distance()

    r = sr.Recognizer()
    r.energy_threshold = 5000
    mic = sr.Microphone(device_index=1)
    # print(sr.Microphone.list_microphone_names())

    with mic as source:
        print("Say now!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 3)

    my_string = r.recognize_google(audio)

    if my_string == 'go':
        Motor_1.clockwise(5)
        Motor_2.c_clockwise(5)
    elif my_string == 'stop':
        Motor_1.stop()
        Motor_2.stop()
    elif my_string == 'left':
        Motor_1.clockwise(5)
        Motor_2.clockwise_slow(5)
    elif my_string == 'right':
        Motor_1.clockwise_slow(5)
        Motor_2.clockwise(5)'''
