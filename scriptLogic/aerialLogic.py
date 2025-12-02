import requests
import re
import os
from scriptLogic.helperFunctions import readUserInstruction, checkImageExisting
from scriptLogic.logs import logRequest, safeRequest


## ===== API (LOAD AN IMAGE FOR A GIVEN ADRESS) ======


# Process one line of instruction: split instruction, get coordinates, get and save areial image
# TODO: Might not be needed anymore
def loadAerialImage(instruction, outputFolder):

    # Split user instruction into location and folder name
    locationFromInput, subfolder = readUserInstruction(instruction)

    # If requested aerial image is already in output folder: save 2 api calls
    if checkImageExisting(os.path.join(outputFolder, subfolder), locationFromInput):
        return

    # Get coordinates and full location name from API
    x, y, locationFromAPI = requestGeoInformation(locationFromInput)

    # if successful, get aerial image from API and save to folder
    if x != '':
        requestAndSaveImage(x, y, locationFromInput, outputFolder, subfolder, zoomLevel = 750)


# Get coordinates and official name of a given location
# TODO: Improve error handling.
def requestGeoInformation(address):
    # Check logs to stay within API limits and wait if necessary
    safeRequest()

    # URL of geocoding API endpoint of GeoAdmin
    url = "https://api3.geo.admin.ch/rest/services/api/SearchServer"

    # Parameters for the API Request
    params = {
        'searchText': address,  # Die Adresse, die geocodiert werden soll
        'type': 'locations',  # Wir suchen nach geokodierten Orten
        'limit': 1,  # Maximale Anzahl der Ergebnisse
        'returnGeometry': 'true',  # Wir wollen die Geometrie (Koordinaten) im Ergebnis
        'sr': '2056'  # Neue Landesvermessung (2...../1....)
    }

    # Send request
    response = requests.get(url, params=params)
    logRequest()

    # Case: Got valid answer
    if response.status_code == 200:
        data = response.json()

        # Check if API found the requested location
        if data['results']:
            # Coordinates, in the swiss coordinate system 'Neue Landesvermessung'
            x = float(data['results'][0]['attrs']['x'])
            y = float(data['results'][0]['attrs']['y'])

            # Official name of location
            # locationNameRaw = data['results'][0]['attrs']['label']
            # locationName = re.sub(r"<.*?>", "", locationNameRaw)
            # print(f'Für den Ort "{locationFromUser}" wurde "{locationName}" gefunden.')

            return x, y
        else:
            print(f'Für den Ort "{address}" kennt GeoAdmin leider keinen Eintrag.')
            return '', ''
    else:
        print(f"Für den Ort {address} ist folgender Fehler aufgetreten:")
        print(f"{response.status_code} - {response.text}")
        return '', ''


# Get aerial image for coordinates and save to given output folder with given file name
def requestAndSaveImage(x, y, zoomLevel, fileName):
    # Check logs to stay within API limits and wait if necessary
    safeRequest()

    try:

        # Calculate image frame with desired zoom level
        minx = x - zoomLevel / 2
        miny = y - zoomLevel / 2
        maxx = x + zoomLevel / 2
        maxy = y + zoomLevel / 2

        # WMS 1.3.0 with EPSG:2056 requires this weired format: (y,x,y,x)
        bbox = f"{miny},{minx},{maxy},{maxx}"

        # Web Map Service API of Geo Admin
        url = "https://wms.geo.admin.ch/?"

        # Parameters for the API Request
        params = {
            "SERVICE": "WMS",
            "VERSION": "1.3.0",
            "REQUEST": "GetMap",
            "LAYERS": "ch.swisstopo.swissimage",
            "STYLES": "",
            "FORMAT": "image/jpeg",
            "TRANSPARENT": "FALSE",
            "CRS": "EPSG:2056",
            "BBOX": f"{bbox}",
            "WIDTH": "800",
            "HEIGHT": "800"
        }

        # Send request
        response = requests.get(url, params=params)
        logRequest()

        # Case: Got results
        if response.status_code == 200:
            try:
                # Create output sub folder in case it doesn't exist yet
                os.makedirs(f'./images', exist_ok=True)

                # Save image
                imagePath = f"./images/{fileName}.jpg"
                with open(imagePath, "wb") as f:
                    f.write(response.content)

                print(f"Luftbild für {fileName} erfolgreich heruntergeladen und als {imagePath} gespeichert.")
                return imagePath

            # Error during saving of the received image
            except IOError as e:
                print(f"Fehler beim speichern des Bildes für {fileName}.")

        # API can be reached but reutrns error code
        else:
            print(f"Die API gab während der Luftbildanfrage für {fileName} folgenden Fehler: {response.status_code} - {response.text}")
            return None

    # API can't be reached
    except requests.exceptions.RequestException as e:
        print(f"Die API konnte nicht erreicht werden (z.B. Netzwerkfehler) für das Bild {fileName}: {e}")
        return None

    # All other errors
    except Exception as e:
        print(f"Es ist ein unerwarteter Fehler während dem Laden des Bildes {fileName} aufgetreten: {e}")
        return None

