from scriptLogic.api import requestGeoInformation, requestAndSaveImage

address = input("Bitte Adresse eingeben: ")
zoomLevel = int(input("Bitte Zoom Level eingeben: "))
x, y = requestGeoInformation(address)

requestAndSaveImage(x, y, zoomLevel, address, 'addressChecker')