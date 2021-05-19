import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()

harvard = sr.AudioFile('audio_files_harvard.wav')
with harvard as source:
    audio = r.record(source)

print(type(audio))
print(r.recognize_google(audio))

jackhammer = sr.AudioFile('audio_files_jackhammer.wav')
with jackhammer as source1:
    r.adjust_for_ambient_noise(source1, duration=0.5)
    audio1 = r.record(source1)

print('                            ')
print(r.recognize_google(audio1))