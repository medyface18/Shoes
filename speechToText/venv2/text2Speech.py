from gtts import gTTS
import os
#Change text to read out whatever is displayed about each attraction
myname = 'Welcome o geeksforgeeks!'
while langSettings != "English" or langSettings != "Spanish" or langSettings != "French" or langSettings != "Chinese"
    langSettings = input("What language would you prefer? English/Spanish/French/Chinese")
    if langSettings == "English":
        language = 'en'
    elif langSettings == "Spanish":
        language = 'spa'
    elif langSettings == "French":
        language = 'fr'
    elif langSettings == "Chinese":
        language = 'es'
    else:
        print()
yes = gTTS(text=myname, lang=language, slow=False)
yes.save("welcome.mp3")
os.system("welcome.mp3")