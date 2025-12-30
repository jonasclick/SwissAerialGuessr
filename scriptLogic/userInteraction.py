import re

## ===== INTERACTIONS WITH USER ON CONSOLE =====

# Display basic explanation about script
def initialExplanationOfScript():
    print("================= SwissAreialGuessr ===================")
    print("===     Wie gut kennst du die Schweiz von oben?     ===")
    print()
    print("Dieses Spiel zeigt dir 10 Luftbilder von Orten in der Schweiz.")
    print("Jeder korrekt erratene Ort gibt einen Punkt.")
    print("Wie viele Orte kannst du erraten?")
    print()
    print('Die Quelle aller gezeigten Luftbilder ist ©swisstopo.')
    print('Weitere Infos unter: https://www.swisstopo.admin.ch/de/analoge-luftbilder')
    print()
    print()


# Get answer from user and check with Regex
def getValidAnswer():
    rawGuess = ''

    validAnswer = False
    while not validAnswer:
        rawGuess = input("Was ist hier für ein Ort abgebildet? ")

        if rawGuess == '':
            print("Bitte keine leere Eingabe machen.")
            continue

        # validate answer of User (Regex)
        forbiddenChars = re.search(r"[!#$%()*+:;<=>?@_{|}§€£¥¡¿«»]", rawGuess)
        if not forbiddenChars:
            validAnswer = True
        else:
            print("Bitte keine Sonderzeichen eingeben.")

    return rawGuess