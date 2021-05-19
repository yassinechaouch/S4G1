import speech_recognition as sr
sr.__version__

r = sr.Recognizer()

harvard = sr.AudioFile('audio_files_harvard.wav')
with harvard as source:
    audio = r.record(source)

r.recognize_google(audio)