#!/usr/bin/env python3

import os
from scriptLogic.userInteraction import initialExplanationOfScript, getInstructionsFromFile, getOutputPath, scriptEnd
from scriptLogic.aerialLogic import loadAerialImage
from scriptLogic.logs import cleanUpLogs
from scriptLogic.consoleColor import setUpConsoleColor

# Set console color to user preference
setUpConsoleColor()

# Disply basic explanation about script to user
initialExplanationOfScript()


# Play one round of SwissAerialGuessr
print("==== EINE NEUE RUNDE BEGINNT =====")
print("Eine Runde besteht aus 10 Bildern, die du erraten musst.")

for i in range(10):
    # Select a random place from the data base

    # Check if place has an associated path to it's image

    # If no path: Check if place has coordinates

    # If no coordinates: Get coordinates from API
    # Get Image for Coordinates (with zoom factor from DB)

    # Save image to images folder, save path to DB

    # Duplicate image to 'aktuelles_Bild.jpg'


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