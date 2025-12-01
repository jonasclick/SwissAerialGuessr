import os

## ====== HELPER FUNCTIONS =======

# Format file path to not end on '/', for empty path return a default path
def formatFilePath(path, defaultPath):
    match path:
        case '':
            return defaultPath
        case p if p.endswith('/'):
            return p[:-1]
        case _:
            return path

# Split one line of user instruction by the ';'
def readUserInstruction(instruction):
    # Split instruction at ';'
    instructionAsList = instruction.split(";")

    return instructionAsList[0], instructionAsList[1]

# Check wheter given file exists at given path
def checkImageExisting(path, locationName):
    # First we check if the subfolder exists
    if not os.path.isdir(path):
        return False

    # If the subfolder exists, we check for an
    # existing image for the requested location
    files = os.listdir(path)
    imageExisting = False

    for file in files:
        file = file.replace('.jpg', '')
        if file == locationName:
            imageExisting = True

    if imageExisting:
        print(f'Im Ordner {path} wurde bereits ein Bild für {locationName} gefunden.')
        print('Das Skript verzichtet auf einen erneuten Download.')

    return imageExisting