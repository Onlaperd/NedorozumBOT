from gtts import gTTS
from playsound import playsound
from os import system

def CreateAudio(TextToConvert, filename):
    try:
        # Create a temporary file in the current working directory
        temp_file = filename + ".mp3"
        
        # Generate the audio file
        obj = gTTS(text=TextToConvert, lang="uk", slow=False)
        obj.save(temp_file)
        
    except Exception as e:
        print(f"Error: {e}")

print("Зачекайте будь-ласка, йде генерація необхідного контенту..")

print("завершено 0%")
CreateAudio("@@@@@@@@@@@", "AShit")
print("завершено 10%")
CreateAudio("ніколи", "NoWhen")
CreateAudio("Слава Україні!", "G1")
CreateAudio("Героям Слава!", "G2")
print("завершено 20%")
CreateAudio("шо-шо, не чує баба", "BabaNeChue")
CreateAudio("Слава Нації!", "G3")
CreateAudio("Смерть ворогам!", "G4")
print("завершено 30%")
CreateAudio("Україна!", "G5")
CreateAudio("Понад усе!", "G6")
CreateAudio("скажи паляниця", "G7")
print("завершено 40%")
CreateAudio("молодець, не москаль", "G8")
CreateAudio("путін Ху... ЛАЛАЛАЛАЛАЛАЛА", "Putin-DickHead")
CreateAudio("Ти занадто бананальний. нудно", "GETOUTAHERE")
print("завершено 50%")
CreateAudio("Що? повтори будь-ласка ще раз бо я не слухав", "Reapeat")
CreateAudio("ШО? НЕ ЧУЮ! Але я всеодно краще за якийсь там 'ChatGPT' ", "IDONOTHEAR")
CreateAudio("зроз", "zroz")
print("завершено 60%")
CreateAudio("все дуже цікаво, але зовсім не зрозуміло", "aga")
CreateAudio("ААААААААААААААААААААААААААААААААААААААААА", "A")
CreateAudio("ніяк", "NoHow")
print("завершено 70%")
CreateAudio("так", "yes")
CreateAudio("ні", "no")
CreateAudio("мабуть", "Maybe")
print("завершено 80%")
CreateAudio("не знаю", "IDK")
CreateAudio("йди в дупу", "GoToAss")
CreateAudio("тому, що", "Because")
print("завершено 90%")
CreateAudio("Привіт, чого тобі треба?", "HelloShort")
CreateAudio("Привіт! Я - NedorozumBOT. Я створений щоб бісити всіх навколо", "hello")
CreateAudio("ніскільки", "NoHowmuch")
print("завершено 99%")

CreateFile = open("Phrases.txt", 'w')
CreateFile.write(""" АААААААААААААААААААААААААААААААААААААААААА
 все дуже цікаво, але зовсім не зрозуміло
 зроз
 ШО? НЕ ЧУЮ! Але я всеодно краще за якийсь там 'ChatGPT'
 Що? повтори будь-ласка ще раз бо я не слухав
 путін Ху... ЛАЛАЛАЛАЛАЛАЛА
 @@@@@@@@@@@
 Слава Україні!""")
CreateFile.close()

CreateFile = open("PhrasesNames.txt", 'w')
CreateFile.write("""A.mp3
aga.mp3
zroz.mp3
IDONOTHEAR.mp3
Reapeat.mp3
Putin-DickHead.mp3
AShit.mp3
G1.mp3""")
CreateFile.close()

input("генерація завершена! Натисніть ENTER щоб запустити NedorozumBOT")
system("python NedorozumBOT.py")