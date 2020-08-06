import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')

# for voice in voices:
#     print("Voice: %s" % voice.name)
#     print(" - ID: %s" % voice.id)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
#     print("\n")

engine.setProperty('rate',170)
engine.setProperty('volume',2.0)
# engine.setProperty("voice", voices[0].id)

def speak_response(text):
    engine.say(text)
    engine.runAndWait()
    return print(text)

# speak_response('Hi prakhar')