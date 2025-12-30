#!/usr/bin/env python3

import os
from scriptLogic.game import displayImage, checkAnswerUsingTokenSet
from scriptLogic.userInteraction import initialExplanationOfScript, getValidAnswer
from scriptLogic.logging.logs import cleanUpLogs
from scriptLogic.consolecolor.consoleColor import setUpConsoleColor
from scriptLogic.database.query import dbInsertUpdateDelete, dbQuery

# BASIC INFO ABOUT SCRIPT
# Kommentare: Am Anfang von wem, wozu? wie aufrufen und ggf. noch Versionen (Änderungshistorie)

# Security und Integration: Nutzer soll rw auf config haben und x auf skript. Skript ohne rw, das ist sicherer.


# Set console color to user preference
setUpConsoleColor()

# Display basic explanation about script to user
initialExplanationOfScript()

# Restart a new game until user wants to end script
endScriptCondition = ''
while endScriptCondition == '':
    # Play SwissAerialGuessr
    print("==== EINE NEUE RUNDE BEGINNT =====")
    print("Eine Runde besteht aus 10 Bildern, die du erraten musst.")
    print("Viel Glück!")
    print("\n" * 4)

    score = 0
    numberOfRounds = 10
    for i in range(numberOfRounds):

        print(f'====== BILD {i+1} VON {numberOfRounds} ======')
        # Get image and correct answer
        print("Ein Luftbild wird vorbereitet...")

        placeToGuess = displayImage()
        if placeToGuess is None:
            # Error while getting image and answer
            print("In diesem Durchgang konnte kein Luftbild geladen werden.")
            continue


        # Ask Answer from User
        print("Die Bilddatei 'aktuellesBild.jpg' liegt nun im Verzeichnis in dem auch dieses Skript liegt.")
        print("Öffne die Bilddatei und rate, was für ein Ort abgebildet ist.")
        print()
        rawGuess = getValidAnswer()
        if rawGuess == '':
            continue


        # Process answer
        isCorrect = checkAnswerUsingTokenSet(rawGuess, placeToGuess, similarityTreshold=78)
        if isCorrect:
            score += 1
            print("==== Korrekt! ====")
        else:
            print("==== Leider nicht korrekt. ====")

        print(f"Der Gesuchte Ort war {placeToGuess}.")
        print("\n" * 3)
        # input("Drücke 'Enter', um das nächste Bild zu laden.")

        # Clear screen ('cls' on Windows, 'clear' on UNIX)
        os.system('cls' if os.name == 'nt' else 'clear')


    # End of Game
    print("===== DIE RUNDE IST VORBEI =======")
    print(f"Du hast {score} von {numberOfRounds} Punkten erzielt.")
    print("\n" * 3)

    # Save score to DB
    dbInsertUpdateDelete(f"INSERT INTO spiel (Punktzahl) VALUES ({score});")

    # Show user stats (total games played, average score)
    statsTupel = dbQuery("SELECT COUNT(*) AS Anzahl, AVG(Punktzahl) AS Durchschnitt FROM spiel;").first()
    if statsTupel is not None:
        print(f"Du hast total {statsTupel.Anzahl} Spiele gespielt.")
        print(f"Du hast durchschnittlich {statsTupel.Durchschnitt:.2f} Punkte erreicht.")
        print("\n" * 3)

    print("Um nochmal eine Runde zu spielen drücke 'Enter'.")
    print("Um das Skript zu beenden, tippe 'Ende'.")
    endScriptCondition = input()


# CLEAN UP
# Delete logging older than a day
cleanUpLogs()

# Reset console color to default
print('\033[0m')