import time
from datetime import datetime, timedelta


## ===== LOGGING in order to stay within API lmits =====

logsInstructions = '''# NOTE: Do not change the contents or name of this file,
# unless you know what you're doing.

# File keeps track of API requests so that the script can
# slow itself down to make sure it doesn't go over the
# fair use limit of 20 requests per minute.


'''


# Log the timestamp of a request to logfile
def logRequest():
    with open("./scriptLogic/logs.txt", "a", encoding="utf-8") as logFile:
        timestamp = datetime.now()
        logFile.write(f'\n{timestamp}')


# Read and return logs from log file
def getLogs():
    # Read the logs
    with open("./scriptLogic/logs.txt", "r", encoding="utf-8") as logFile:
        logData = logFile.read()

    cleanLogs = []
    logsRaw = logData.splitlines()

    # [] Remove the instruction text
    for line in logsRaw[8:]:
        line = line.strip()
        if line == "":
            continue
        try:
            datetime.fromisoformat(line)
            cleanLogs.append(line)
        except:
            continue
    return cleanLogs


# Read logs and check if more than 20 requests have been made in the past minute
def requestAllowed():
    # API Rate limit in requests per Minute
    requestsPerMinuteAllowed = 20

    logs = getLogs()

    oneMinuteAgo = datetime.now() - timedelta(minutes=1)
    pastMinute = 0

    for log in logs:
        dateTimeObject = datetime.fromisoformat(log)
        if dateTimeObject >= oneMinuteAgo:
            pastMinute += 1

    if pastMinute >= requestsPerMinuteAllowed:
        return False
    else:
        return True


# Stops execution until an API call can be safely made
# without going over the api limit
def safeRequest():
    while not requestAllowed():
        print("Das Skript wartet, um den API-Dienst nicht zu überlasten...")
        time.sleep(3)


def cleanUpLogs():
    logs = getLogs()
    oneDayAgo = datetime.now() - timedelta(days=1)

    recentLogs = [log for log in logs if datetime.fromisoformat(log) >= oneDayAgo]

    with open("./scriptLogic/logs.txt", "w", encoding="utf-8") as logFile:
        logFile.write(logsInstructions)

        for log in recentLogs:
            print(log, file=logFile)
