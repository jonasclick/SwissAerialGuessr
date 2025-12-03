import os
import re
import shutil
from fuzzywuzzy import fuzz
from scriptLogic.api import requestGeoInformation, requestAndSaveImage
from scriptLogic.query import dbInsertUpdateDelete, dbQuery



# Get a random place from DB,
# get its image from chache or API
# save image as ./aktuellesBild.jpg
def displayImage():

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
        return None
    except Exception as e:
        print(f'Allgemeiner Fehler beim Kopieren des Bildes: {e}')
        return None

    return placeTupel.Name


# Clean a text to improve accuracy in comparisons
# Should be used to clean user input and correct place name from DB
def cleanInput(text):
    # Remove leading, trailing spaces and make all lower case
    text = text.strip().lower()

    # Replace Umlaute, accents and other symbols
    # this also helps with location names containing a "." (St.Gallen etc.)
    replacements = {
        'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'é': 'e', 'è': 'e', 'à': 'a', 'ç': 'c',
        '-': ' ', '/': ' ', '.': ' '
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    # Replace all types of white spaces with a simple ' '
    text = re.sub(r'\s+', ' ', text)

    return text


# Compare user answer to correct answer: Calculate similarity and rate user answer
def checkAnswerUsingTokenSet(correctAnswer, userGuess, similarityTreshold=80):

    # Clean both strings
    correctAnswerClean = cleanInput(correctAnswer)
    correctGuessClean = cleanInput(userGuess)

    # Calculate similarity using 'token set ratio' algorithm by fuzzywuzzy
    similarity = fuzz.token_set_ratio(correctAnswerClean, correctGuessClean)
    print(f"Deine Antwort hat eine Ähnlichkeit von {similarity}% zum gesuchten Ort.")

    # Rate Answer
    if similarity >= similarityTreshold:
        return True
    else:
        return False