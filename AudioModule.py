import speech_recognition as sr
import os

from gtts import gTTS
from playsound import playsound


def RecordAudio():
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='uk-UK')
        return query.lower()
    except sr.UnknownValueError:
        print("[NedorozumBOT] Шо-шо? Не чує баба")
        playsound("BabaNeChue.mp3")
        return ""
    except sr.RequestError as e:
        print(f"[NedorozumBOT] Помилка під час обробки вашого брєду: {e}")
        return ""


def CreateAudio(text_to_convert, filename):
    try:
        temp_file = f"{filename}.mp3"

        # Check if the file already exists
        if not os.path.exists(temp_file):
            obj = gTTS(text=text_to_convert, lang="uk", slow=False)
            obj.save(temp_file)

    except Exception as e:
        print(f"[NedorozumBOT] Помилка під час обробки вашого брєду: {e}")


if __name__ == "__main__":
    print("This is not a main file.")
    os.startfile("NedorozumBOT.py")
