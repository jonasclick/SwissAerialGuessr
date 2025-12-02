#!/usr/bin/env python3

import os
import shutil
from scriptLogic.userInteraction import initialExplanationOfScript, getInstructionsFromFile, getOutputPath, scriptEnd
from scriptLogic.aerialLogic import loadAerialImage
from scriptLogic.logs import cleanUpLogs
from scriptLogic.consoleColor import setUpConsoleColor
from scriptLogic.query import dbQuery, dbInsertUpdateDelete
from scriptLogic.aerialLogic import requestGeoInformation, requestAndSaveImage


# Set console color to user preference
setUpConsoleColor()

# Disply basic explanation about script to user
initialExplanationOfScript()


# Play one round of SwissAerialGuessr
print("==== EINE NEUE RUNDE BEGINNT =====")
print("Eine Runde besteht aus 10 Bildern, die du erraten musst.")

for i in range(10):

    # TODO: Müsste man hier noch mit While loopen bis ein Bild gefunden wurde??
    foundImageToDisplay = False
    while not foundImageToDisplay:
        # Select a random place from the data base
        placeTupel = dbQuery("SELECT * FROM ort ORDER BY RAND() LIMIT 1;").first()
        if placeTupel is None:
            # Restart loop
            continue
        print(placeTupel)

        # if place doesn't have an associated path to it's image
        # or place should reload it's image (updateFlag == 1)
        if placeTupel.PfadBild is None or placeTupel.updateFlag == 1:
            print('Image needs to be (re)loaded.')

            # If no path and no coordinates available: get coordinates
            if placeTupel.Ostwert is None or placeTupel.Nordwert is None:
                # If no coordinates: Get coordinates from API
                x, y = requestGeoInformation(placeTupel.Adresse)


            # Get Image for Coordinates (with zoom factor from DB) and save to images folder
            imagePath = requestAndSaveImage(x, y, placeTupel.Zoom, placeTupel.Adresse)
            if imagePath is not None:
                foundImageToDisplay = True
                # save image path to db
                if dbInsertUpdateDelete(f"UPDATE ort SET Ostwert = {x}, Nordwert = {y}, updateFlag = 0 WHERE ID_Ort = {placeTupel.ID_Ort}"):
                    print("Successfully saved coordinates to DB.")
            else:
                # Image couldn't be downloaded from API
                continue
        else:
            # Got a place, place has path to image
            foundImageToDisplay = True

    # place has a path to it's image:
    # Duplicate image to 'aktuelles_Bild.jpg'
    destinationPath = './aktuellesBild.jpg'
    try:
        shutil.copy(imagePath, destinationPath)
    except FileNotFoundError:
        print(f'Bild am Quellordner {imagePath} konnte nicht gefunden werden.')
    except Exception as e:
        print(f'Allgemeiner Fehler beim Kopieren des Bildes: {e}')


    # Ask Answer from User
    print("Die Bilddatei 'aktuelles_Bild.jpg' liegt nun im Verzeichnis in dem auch dieses Skript liegt.")
    print("Öffne die Bilddatei und rate, was für ein Ort abgebildet ist.")
    rawGuess = input("Was ist hier für ein Ort abgebildet? ")

# Get instructions from user
instructionsList = getInstructionsFromFile()

# Get path to output folder for aerial images
outputFolder = getOutputPath()

# Create output folder if it doesn't exist yet
os.makedirs(f'./{outputFolder}', exist_ok=True)

# Get and save aerial image for each instruction
for instruction in instructionsList:
    if not instruction.startswith('#'): # Ignore commented lines
        loadAerialImage(instruction, outputFolder)

# Inform user about end of script
scriptEnd()



# CLEAN UP
# only keep logs which are older than a day
cleanUpLogs()

# Reset console color to default
print('\033[0m')