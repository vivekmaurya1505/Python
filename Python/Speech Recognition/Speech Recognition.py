import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speck:")
    audio = r.listen(source)
    try:
        output = r.recognize_google(audio)
        print("you said:{}",format(output))

    except:
        print("I can't recognize what you said please speck clearly")
