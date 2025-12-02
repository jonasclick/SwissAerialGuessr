#!/usr/bin/env python3

import re
import os
from scriptLogic.game import displayImage, checkAnswerUsingTokenSet
from scriptLogic.userInteraction import initialExplanationOfScript, scriptEnd
from scriptLogic.logs import cleanUpLogs
from scriptLogic.consoleColor import setUpConsoleColor
from scriptLogic.query import dbInsertUpdateDelete

# Set console color to user preference
setUpConsoleColor()

# Disply basic explanation about script to user
initialExplanationOfScript()


# Play SwissAerialGuessr
print("==== EINE NEUE RUNDE BEGINNT =====")
print("Eine Runde besteht aus 10 Bildern, die du erraten musst.")
print("Viel Glück!")
print("\n" * 4)

score = 0
for i in range(10):

    # Get image and correct answer
    print("Ein Luftbild wird geladen...")

    answer = displayImage()
    if answer is None:
        # Error while getting image and answer
        print("In diesem Durchgang konnte kein Luftbild geladen werden.")
        continue


    # Ask Answer from User
    print("Die Bilddatei 'aktuelles_Bild.jpg' liegt nun im Verzeichnis in dem auch dieses Skript liegt.")
    print("Öffne die Bilddatei und rate, was für ein Ort abgebildet ist.")
    print()

    rawGuess = ''
    validAnswer = False
    while not validAnswer:
        rawGuess = input("Was ist hier für ein Ort abgebildet? ")

        # validate answer of User (Regex)
        forbiddenChars = re.search(r"[!#$%()*+:;<=>?@_{|}§€£¥¡¿«»]", rawGuess)
        if not forbiddenChars:
            validAnswer = True
        else:
            print("Die Eingabe war ungültig. Bitte keine Sonderzeichen eingeben.")

    # Process answer
    isCorrect = checkAnswerUsingTokenSet(rawGuess, answer, similarityTreshold=70)
    if isCorrect:
        score += 1
        print("==== Korrekt! ====")
    else:
        print("Leider nicht korrekt.")

    print(f"Der Gesuchte Ort war {answer}.")
    print("\n" * 3)
    input("Drücke 'Enter', um das nächste Bild zu laden.")

    # Clear screen ('cls' on Windows, 'clear' on UNIX)
    os.system('cls' if os.name == 'nt' else 'clear')


# End of Game
print("===== DIE RUNDE IST VORBEI =======")
print(f"Du hast {score} von 10 Punkten erzielt.")

dbInsertUpdateDelete(f"INSERT INTO spiel (Punktzahl) VALUES ({score});")















# Inform user about end of script
scriptEnd()

# CLEAN UP
# only keep logs which are older than a day
cleanUpLogs()

# Reset console color to default
print('\033[0m')
