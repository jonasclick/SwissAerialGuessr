#!/usr/bin/env python3

import os
import time

from scriptLogic.game import displayImage, checkAnswerUsingTokenSet
from scriptLogic.userInteraction import initialExplanationOfScript, getValidAnswer
from scriptLogic.logging.logs import cleanUpLogs
from scriptLogic.consolecolor.consoleColor import setUpConsoleColor
from scriptLogic.database.query import dbInsertUpdateDelete, dbQuery

"""
================================================================================
PROJECT:        SwissAerialGuessr
AUTHOR:         Jonas Vetsch, jve161514@stud.gibb.ch
VERSION:        1.4.0 (2025-12-30)
DESCRIPTION:    Interaktives Ratespiel basierend auf Schweizer Luftbildern (©swisstopo).
                Nutzt die GeoAdmin API (WMS) und fuzzywuzzy zur Validierung der Antworten.

USAGE:          Datenbank erstellen und Daten importieren gemäss ./scriptLogic/database
                Mit Python das Skript ./main.py ausführen (Benötigt Python 3.x und die Abhängigkeiten unter ./requirements.txt)

VERSIONS:        
    2025-12-30: v1.4.0 – Optimierung der Validierung & Fuzzy Matching
    2025-12-29: v1.3.1 – Fix der Daten-Synchronisation
    2025-12-22: v1.3.0 – Datenbank vergrössern und bereinigen
    2025-12-18: v1.2.0 – Robustheit & Errorhandling
    2025-12-15: v1.1.0 – Datenbank-Anbindung & Datenverarbeitung
    2025-12-08: v1.0.0 – Initialer Prototyp (Proof of Concept)
================================================================================
"""

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
        time.sleep(2)

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