#!/usr/bin/env python3

import os
import shutil
from scriptLogic.userInteraction import initialExplanationOfScript, scriptEnd
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

    foundImageToDisplay = False
    while not foundImageToDisplay:
        # Select a random place from the data base
        placeTupel = dbQuery("SELECT * FROM ort ORDER BY RAND() LIMIT 1;").first()
        if placeTupel is None:
            # Restart loop
            print("Didn't get a place from DB. Trying again...")
            continue

        # Check if image needs to be loaded from API or from cache (= ./images)
        imagesFolder = './scriptLogic/images'
        imageName = f'{placeTupel.Adresse}.jpg'
        pathToImage = os.path.join(imagesFolder, imageName)

        # Should Image be loaded from API?
        if not os.path.exists(pathToImage) or placeTupel.UpdateFlag == 1:
            print('Image needs to be (re)loaded.')

            # no coordinates available? get coordinates
            if placeTupel.Ostwert is None or placeTupel.Nordwert is None:
                # If no coordinates: Get coordinates from API
                x, y = requestGeoInformation(placeTupel.Adresse)
            else:
                # DB already has coordinates for place, let's access them here:
                x = placeTupel.Ostwert
                y = placeTupel.Nordwert

            # Get Image for Coordinates (with zoom factor from DB) and save to images folder
            foundImageToDisplay = requestAndSaveImage(x, y, placeTupel.Zoom, placeTupel.Adresse, imagesFolder)
            if foundImageToDisplay:
                # save image path to db
                if dbInsertUpdateDelete(f"UPDATE ort SET Ostwert = {x}, Nordwert = {y}, updateFlag = 0 WHERE ID_Ort = {placeTupel.ID_Ort}"):
                    print("Successfully saved coordinates to DB.")
            else:
                print("Image couldn't be downloaded from API. Trying another place now.")
                continue
        else:
            # Image to place already exists in cache and doesn't need to be reloaded
            foundImageToDisplay = True

    # Duplicate image to 'aktuelles_Bild.jpg'
    destinationPath = './aktuellesBild.jpg'
    try:
        shutil.copy(pathToImage, destinationPath)
    except FileNotFoundError:
        print(f'Bild an der Quelle {pathToImage} konnte nicht gefunden werden.')
    except Exception as e:
        print(f'Allgemeiner Fehler beim Kopieren des Bildes: {e}')


    # Ask Answer from User
    print("Die Bilddatei 'aktuelles_Bild.jpg' liegt nun im Verzeichnis in dem auch dieses Skript liegt.")
    print("Öffne die Bilddatei und rate, was für ein Ort abgebildet ist.")
    rawGuess = input("Was ist hier für ein Ort abgebildet? ")

    # Process Answer of User







# Inform user about end of script
scriptEnd()

# CLEAN UP
# only keep logs which are older than a day
cleanUpLogs()

# Reset console color to default
print('\033[0m')