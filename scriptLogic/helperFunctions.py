import platform
import subprocess
import os
from pathlib import Path


# Try to open the file at a given path
def openImage(pathRelative):
    # create path object from relative path
    pathObject = Path(pathRelative)

    # convert to absolute path
    pathAbsolute = pathObject.resolve()

    # check if file exists before trying to open it
    if not pathAbsolute.exists():
        print(f"Fehler beim Öffnen der Datei: Die Datei '{pathAbsolute}' wurde nicht gefunden.")
        return

    # check operating system name
    system = platform.system()

    try:
        if system == 'Windows':
            # Windows
            os.startfile(pathAbsolute)
        elif system == 'Darwin':
            # macOS
            subprocess.run(['open', str(pathAbsolute)], check=True)
        else:
            # Linux and other os
            subprocess.run(['xdg-open', str(pathAbsolute)], check=True)

        print(f"Öffne: {pathAbsolute.name}")

    except Exception as e:
        print(f"Ein Fehler ist während dem Öffnen der Datei aufgetreten: {e}")