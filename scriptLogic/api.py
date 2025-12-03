import requests
import os
from scriptLogic.logs import logRequest, safeRequest


## ===== API (LOAD AN IMAGE FOR A GIVEN ADRESS) ======

# Get coordinates and official name of a given location
def requestGeoInformation(address):
    safeRequest() # Check logs to stay within API limits and wait if necessary

    try:
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

        # Valid answer from API
        if response.status_code == 200:
            try:
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
                    return None
            except Exception as e:
                print(f'Fehler beim Lesen der Koordinaten in der Antwort der Search-Server-API: {e}')
                return None

        # Status Code from API raises an issue
        else:
            print(f"Für den Ort {address} ist folgender Fehler aufgetreten:")
            print(f"{response.status_code} - {response.text}")
            return None

    # API can't be reached
    except requests.exceptions.RequestException as e:
        print(f"Die API konnte nicht erreicht werden (z.B. Netzwerkfehler) um die Koordinaten für {address} aufzulösen: {e}")
        return None

    # All other errors
    except Exception as e:
        print(f"Es ist ein unerwarteter Fehler während dem Auflösen der Koordinaten für {address} aufgetreten: {e}")
        return None



# Get aerial image for coordinates and save to given output folder with given file name
def requestAndSaveImage(x, y, zoomLevel, address, pathToImages):
    safeRequest() # Check logs to stay within API limits and wait if necessary

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
            "WIDTH": "4000",
            "HEIGHT": "4000"
        }

        # Send request
        response = requests.get(url, params=params)
        logRequest()

        # Case: Got results
        if response.status_code == 200:
            try:
                # Create output sub folder in case it doesn't exist yet
                os.makedirs(pathToImages, exist_ok=True)

                # Save image
                imagePath = f"{pathToImages}/{address}.jpg"
                with open(imagePath, "wb") as f:
                    f.write(response.content)

                # print(f"Luftbild für {address} erfolgreich heruntergeladen und als {imagePath} gespeichert.")
                return True

            # Error during saving of the received image
            except IOError as e:
                print(f"Fehler beim speichern des Bildes für {address}.")

        # API can be reached but reutrns error code
        else:
            print(f"Die API gab während der Luftbildanfrage für {address} folgenden Fehler: {response.status_code} - {response.text}")
            return False

    # API can't be reached
    except requests.exceptions.RequestException as e:
        print(f"Die API konnte nicht erreicht werden (z.B. Netzwerkfehler) für das Bild {address}: {e}")
        return False

    # All other errors
    except Exception as e:
        print(f"Es ist ein unerwarteter Fehler während dem Laden des Bildes {address} aufgetreten: {e}")
        return False

