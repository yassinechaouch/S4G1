import speech_recognition as sr
r = sr.Recognizer()

mic = sr.Microphone()

#sr.Microphone.list_microphone_names()

#mic = sr.Microphone(device_index=3)

with mic as source:
    audio = r.listen(source)

r.recognize_google(audio)

'''with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)'''
