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

def CreateAudio(TextToConvert, filename):
    try:
        temp_file = f"{filename}.mp3"

        # Check if the file already exists
        if not os.path.exists(temp_file):
            obj = gTTS(text=TextToConvert, lang="uk", slow=False)
            obj.save(temp_file)

    except Exception as e:
        print(f"Error: {e}")

def run():
    print("[NedorozumBOT] Привіт! Я - NedorozumBOT. Я створений щоб бісити всіх навколо")
    playsound("hello.mp3")

    while True:
        print("[NedorozumBOT] ...")
        try:
            RecordedAudio = " " + RecordAudio()
            print(f"[You] {RecordedAudio}")

            HowCount = RecordedAudio.count("як ")
            WhenCount = RecordedAudio.count("коли ")
            ACount = RecordedAudio.count(" а ")
            HelloCount = RecordedAudio.count("привіт")
            HowAreYouCount = RecordedAudio.count("як справи")
            WhyCount = RecordedAudio.count("чому ")
            HowMuchCount = RecordedAudio.count("скільки")

            if RecordedAudio == "":
                pass
            elif HowAreYouCount > 0:
                print("[NedorozumBOT] Ти занадто бананальний. нудно")
                playsound("GETOUTAHERE.mp3")
                input("[натисніть ENTER щоб закрити програму]")
                exit()
            elif HelloCount > 0:
                print("[NedorozumBOT] Привіт, чого тобі треба?")
                playsound("HelloShort.mp3")
            elif RecordedAudio.lower() == " слава україні":
                print("[NedorozumBOT] Героям Слава!")
                playsound("G2.mp3")
            elif RecordedAudio.lower() == " героям слава":
                print("[NedorozumBOT] Слава Нації!")
                playsound("G3.mp3")
            elif RecordedAudio.lower() == " слава нації":
                print("[NedorozumBOT] Смерть Ворогам!")
                playsound("G4.mp3")
            elif RecordedAudio.lower() == " смерть ворогам":
                print("[NedorozumBOT] Україна!")
                playsound("G5.mp3")
            elif RecordedAudio.lower() == " україна":
                print("[NedorozumBOT] Понад Усе!")
                playsound("G6.mp3")
            elif RecordedAudio.lower() == " понад усе":
                print("[NedorozumBOT] скажи паляниця")
                playsound("G7.mp3")
            elif RecordedAudio.lower() == " паляниця":
                print("[NedorozumBOT] молодець, не москаль")
                playsound("G8.mp3")
            elif HowCount > 0:
                print("[NedorozumBOT] ніяк")
                playsound("NoHow.mp3")
            elif WhenCount > 0:
                print("[NedorozumBOT] ніколи")
                playsound("NoWhen.mp3")
            elif WhyCount > 0:
                print("[NedorozumBOT] тому, що")
                playsound("Because.mp3")
            elif HowMuchCount > 0:
                print("[NedorozumBOT] ніскільки")
                playsound("NoHowmuch.mp3")
            elif ACount > 0:
                WhatToSay = choice(["yes.mp3", "no.mp3", "maybe.mp3", "IDK.mp3", "GoToAss.mp3"])
                if WhatToSay == "yes.mp3":
                    print("[NedorozumBOT] так")
                elif WhatToSay == "no.mp3":
                    print("[NedorozumBOT] ні")
                elif WhatToSay == "maybe.mp3":
                    print("[NedorozumBOT] мабуть")
                elif WhatToSay == "IDK.mp3":
                    print("[NedorozumBOT] не знаю")
                elif WhatToSay == "GoToAss.mp3":
                    print("[NedorozumBOT] йди в дупу")
            else:
                WhatToSaylist = open("PhrasesNames.txt", "r").read().split("\n")
                ChoosedOption = randint(0, len(WhatToSaylist) - 1)

                TextVersion = open("Phrases.txt", "r").read().split("\n")

                print(f"[NedorozumBOT] {TextVersion[ChoosedOption]}")
                playsound(WhatToSaylist[ChoosedOption])

                Data = open("Phrases.txt", "a")
                Data.write(RecordedAudio + "\n")
                Data.close()

                Data = open("PhrasesNames.txt", "r")
                TMP = Data.read()
                TMP1 = TMP.split("\n")
                HowMuchExistsAlready = len(TMP1)
                print(HowMuchExistsAlready)
                Data.close()

                Data = open("PhrasesNames.txt", "a")
                Data.write(f"UG{HowMuchExistsAlready}.mp3\n")
                Data.close()

                CreateAudio(RecordedAudio, f"UG{HowMuchExistsAlready}")

        except Exception as e:
            print("[NedorozumBOT] Шо-шо? Не чує баба")
            playsound("BabaNeChue.mp3")
            print(e)

if __name__ == "__main__":
    run()
