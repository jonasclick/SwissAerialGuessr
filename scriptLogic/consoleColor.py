import re
from pathlib import Path

## ===== CONSOLE COLOR LOGIC ======

PathToConfigFile = Path("./config.txt")

def writeConsoleColorConfig(colorCode):
    with open(PathToConfigFile, "w", encoding="utf-8") as configFile:
        configFile.write(colorCode)
        print(f"Deine bevorzugte Konsolenfarbe wurde unter {PathToConfigFile} gespeichert.")
        print(f"Um die bevorzugte Konsolenfarbe zu ändern, lösche die Datei '{PathToConfigFile}' und starte das Skript neu.")

def setUpConsoleColor():
    # No config file found: Ask prefered console color from user and write config file
    if not PathToConfigFile.exists():
        print("Welche Schriftfarbe möchtest du auf der Konsole haben?")
        print("1 = Standard, 2 = blau, 3 = grün")

        userInputAccepted = False
        while not userInputAccepted:
            userInput = input('Bitte Zahl eingeben: ')
            if re.fullmatch(r"^[1-3]$", userInput):
                match int(userInput):
                    case 1:
                        # Standard console color
                        writeConsoleColorConfig('\033[0m')
                    case 2:
                        # Blue
                        writeConsoleColorConfig('\033[34m')
                    case 3:
                        # Green
                        writeConsoleColorConfig('\033[32m')
                    case _:
                        print("Die Eingabe konnte nicht zugeordnet werden.")

                userInputAccepted = True


    # Set console color to user preference
    with open(PathToConfigFile, "r", encoding="utf-8") as configFile:
        colorCode = configFile.read().strip()
        # Set conosle to desired color
        print(colorCode)
