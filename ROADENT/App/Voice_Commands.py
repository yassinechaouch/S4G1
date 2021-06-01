import speech_recognition as sr

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
        forward(5)
    elif x == 'stop':
        STOP()
    elif x == 'left':
        LEFT(5)
    elif x == 'right':
        RIGHT(5)
