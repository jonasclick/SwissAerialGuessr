from scriptLogic.helperFunctions import formatFilePath
import os
import tempfile

## ===== INTERACTIONS WITH USER ON CONSOLE =====

# Display basic explanation about script
def initialExplanationOfScript():
    print("===             SwissAreialGuessr                   ===")
    print("=== Wie gut kennst du die Schweiz aus der Luft?     ===")
    print()
    print("Dieses Spiel zeigt dir 10 Luftbilder von Orten in der Schweiz.")
    print("Jeder korrekt erratene Ort gibt einen Punkt.")
    print("Wie viele Orte kannst du erraten?")
    print()
    print()


# Ask user to specify path to instruction file (text file with places)
def getInstructionsFromFile():
    approved = False
    while not approved:
        # Get instruction file path from user
        print("Standardmässig erwartet das Skript, dass die Instruktionsdatei im selben Ordner liegt wie das Skript.")
        pathFromUser = input("Falls die Datei an einem anderen Ort liegt, gebe den Pfad ein (ansonsten drücke einfach Enter): ")
        path = formatFilePath(pathFromUser, '.')

        # Read text file with instructions
        try:
            with open(f"{path}/input.txt", "r", encoding="utf-8") as instructionFile:
                instructionsRaw = instructionFile.read()

        # Unsuccessful file access
        except Exception as exception:
            print("Beim Lesen der Instruktionsdatei ist ein Fehler aufgetreten:")
            print(exception)
            print()
            print("Stelle sicher, dass das Skript Zugriff auf die Datei hat und gebe den Pfad erneut an.")

        # Successful file access
        else:
            approved = True
            return instructionsRaw.splitlines()


# Ask user to specify path for output of script results
def getOutputPath():
    approved = False
    while not approved:
        print("Gebe den Pfad für die Ausgabe der Luftbilder an. ")
        pathFromUser = input("Ohne Eingabe (nur Enter-Taste) werden die Bilder in ./output gespeichert: ")
        path = formatFilePath(pathFromUser, './output')

        # Validate output folder
        try:
            # Check if output folder exists, else create it
            os.makedirs(path, exist_ok=True)

            # Create temporary file to check write permissions in output folder
            testfile = tempfile.TemporaryFile(dir=path)
            testfile.close()

        # Invalid output folder
        except Exception as exception:
            print("Beim Versuch auf den angegebenen Ausgabeordner zuzugreifen gabe es einen Fehler.")
            print(exception)
            print()
            print("Bitte versuche es nochmal.")

        # Valid output folder
        else:
            approved = True
            print() # Empty line for better visual separation on console
            return path


# Script end text
def scriptEnd():
    print() # Empty line for better visual separation on console
    print('Das Skript hat alle Instruktionen verarbeitet und endet nun.')

