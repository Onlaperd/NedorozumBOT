import os
from random import choice, randint
from sys import exit

import speech_recognition as sr
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


def run():
    print("[NedorozumBOT] Привіт! Я - NedorozumBOT. Я створений щоб бісити всіх навколо")
    playsound("hello.mp3")

    while True:
        print("[NedorozumBOT] ...")
        try:
            recorded_audio = " " + RecordAudio()
            print(f"[You] {recorded_audio}")

            how_count = recorded_audio.count("як ")
            when_count = recorded_audio.count("коли ")
            a_count = recorded_audio.count(" а ")
            hello_count = recorded_audio.count("привіт")
            how_are_you_count = recorded_audio.count("як справи")
            why_count = recorded_audio.count("чому ")
            how_much_count = recorded_audio.count("скільки")

            if recorded_audio == "":
                pass
            elif how_are_you_count > 0:
                print("[NedorozumBOT] Ти занадто бананальний. нудно")
                playsound("GETOUTAHERE.mp3")
                input("[натисніть ENTER щоб закрити програму]")
                exit()
            elif hello_count > 0:
                print("[NedorozumBOT] Привіт, чого тобі треба?")
                playsound("HelloShort.mp3")
            elif recorded_audio.lower() == " слава україні":
                print("[NedorozumBOT] Героям Слава!")
                playsound("G2.mp3")
            elif recorded_audio.lower() == " героям слава":
                print("[NedorozumBOT] Слава Нації!")
                playsound("G3.mp3")
            elif recorded_audio.lower() == " слава нації":
                print("[NedorozumBOT] Смерть Ворогам!")
                playsound("G4.mp3")
            elif recorded_audio.lower() == " смерть ворогам":
                print("[NedorozumBOT] Україна!")
                playsound("G5.mp3")
            elif recorded_audio.lower() == " україна":
                print("[NedorozumBOT] Понад Усе!")
                playsound("G6.mp3")
            elif recorded_audio.lower() == " понад усе":
                print("[NedorozumBOT] скажи паляниця")
                playsound("G7.mp3")
            elif recorded_audio.lower() == " паляниця":
                print("[NedorozumBOT] молодець, не москаль")
                playsound("G8.mp3")
            elif how_count > 0:
                print("[NedorozumBOT] ніяк")
                playsound("NoHow.mp3")
            elif when_count > 0:
                print("[NedorozumBOT] ніколи")
                playsound("NoWhen.mp3")
            elif why_count > 0:
                print("[NedorozumBOT] тому, що")
                playsound("Because.mp3")
            elif how_much_count > 0:
                print("[NedorozumBOT] ніскільки")
                playsound("NoHowmuch.mp3")
            elif a_count > 0:
                what_to_say = choice(["yes.mp3", "no.mp3", "maybe.mp3", "IDK.mp3", "GoToAss.mp3"])
                if what_to_say == "yes.mp3":
                    print("[NedorozumBOT] так")
                elif what_to_say == "no.mp3":
                    print("[NedorozumBOT] ні")
                elif what_to_say == "maybe.mp3":
                    print("[NedorozumBOT] мабуть")
                elif what_to_say == "IDK.mp3":
                    print("[NedorozumBOT] не знаю")
                elif what_to_say == "GoToAss.mp3":
                    print("[NedorozumBOT] йди в дупу")
            else:
                what_to_say_list = open("PhrasesNames.txt", "r").read().split("\n")
                choosed_option = randint(0, len(what_to_say_list) - 1)

                text_version = open("Phrases.txt", "r").read().split("\n")

                print(f"[NedorozumBOT] {text_version[choosed_option]}")
                playsound(what_to_say_list[choosed_option])

                data = open("Phrases.txt", "a")
                data.write(recorded_audio + "\n")
                data.close()

                data = open("PhrasesNames.txt", "r")
                tmp = data.read()
                tmp1 = tmp.split("\n")
                how_much_exists_already = len(tmp1)
                data.close()

                data = open("PhrasesNames.txt", "a")
                data.write(f"UG{how_much_exists_already}.mp3\n")
                data.close()

                CreateAudio(recorded_audio, f"UG{how_much_exists_already}")

        except Exception as e:
            print("[NedorozumBOT] Шо-шо? Не чує баба")
            playsound("BabaNeChue.mp3")
            print(e)

if __name__ == "__main__":
    run()
