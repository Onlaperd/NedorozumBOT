from random import choice, randint
from sys import exit
from AudioModule import *
from playsound import playsound


def AnalyseMessage(recorded_audio):
    if recorded_audio == "":
        pass
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
    elif "як справи" in recorded_audio:
        print("[NedorozumBOT] Ти занадто бананальний. нудно")
        playsound("GETOUTAHERE.mp3")
        input("[натисніть ENTER щоб закрити програму]")
        exit()
    elif "привіт" in recorded_audio:
        print("[NedorozumBOT] Привіт, чого тобі треба?")
        playsound("HelloShort.mp3")
    elif "як " in recorded_audio:
        print("[NedorozumBOT] ніяк")
        playsound("NoHow.mp3")
    elif "коли " in recorded_audio:
        print("[NedorozumBOT] ніколи")
        playsound("NoWhen.mp3")
    elif "чому " in recorded_audio:
        print("[NedorozumBOT] тому, що")
        playsound("Because.mp3")
    elif "скільки" in recorded_audio:
        print("[NedorozumBOT] ніскільки")
        playsound("NoHowmuch.mp3")
    elif " а " in recorded_audio:
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

        # answering user
        with open("PhrasesNames.txt", "r") as create_what_to_say_list:
            what_to_say_list = create_what_to_say_list.read().split("\n")
        choosed_option = randint(0, len(what_to_say_list) - 1)
        with open("Phrases.txt", "r") as create_text_version:
            text_version = create_text_version.read().split("\n")
        print(f"[NedorozumBOT] {text_version[choosed_option]}")
        playsound(what_to_say_list[choosed_option])

        # saving data got from user
        with open("Phrases.txt", "a") as data:
            data.write(recorded_audio + "\n")
        with open("PhrasesNames.txt", "r") as data:
            tmp = data.read().split("\n")
            how_much_exists_already = len(tmp)
        with open("PhrasesNames.txt", "a") as data:
            data.write(f"UG{how_much_exists_already}.mp3\n")
        CreateAudio(recorded_audio, f"UG{how_much_exists_already}")


def run():
    print("[NedorozumBOT] Привіт! Я - NedorozumBOT. Я створений щоб бісити всіх навколо")
    playsound("hello.mp3")

    while True:
        print("[NedorozumBOT] ...")
        try:
            recorded_audio = " " + RecordAudio()
            print(f"[You] {recorded_audio}")

            AnalyseMessage(recorded_audio)

        except Exception as e:
            print("[NedorozumBOT] Шо-шо? Не чує баба")
            playsound("BabaNeChue.mp3")
            print(f"недорозумБОТ видав помилку: {e}")

if __name__ == "__main__":
    run()
