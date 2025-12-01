import os
from scriptLogic.userInteraction import initialExplanationOfScript, getInstructionsFromFile, getOutputPath, scriptEnd
from scriptLogic.aerialLogic import loadAerialImage
from scriptLogic.logs import cleanUpLogs

# Disply basic explanation about script to user
initialExplanationOfScript()

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

# only keep logs
cleanUpLogs()