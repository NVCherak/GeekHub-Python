import re
import csv
import os

file_path = "./reports/"
directory = os.path.dirname(file_path)

if not os.path.exists(directory):
    os.makedirs(directory)

logFile = open('openerp-server.log')

regexDateTime = "\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}"
regexBeforeDescription = "^\s\w+\s|\s\?\s"
markers = ["WARNING", "ERROR", "CRITICAL"]

currentLine = logFile.readline()
lineId = 1

while currentLine:
    for marker in markers:
        search = re.search(marker, currentLine)
        if search:
            date_time = re.search(regexDateTime, currentLine)
            lineAfterMarker = currentLine[search.end():-1]
            description = re.sub(regexBeforeDescription, "", lineAfterMarker)
            with open("./reports/all_data.csv", "a") as csvFile:
                csvWrite = csv.writer(csvFile) # quoting=csv.QUOTE_NONE, escapechar='\\')
                csvWrite.writerow([lineId, marker, date_time.group(), description])
            continue

    currentLine = logFile.readline()
    lineId += 1

logFile.close()

all_dataReader = csv.reader(open('./reports/all_data.csv', 'r'))
uniqueWriter = csv.writer(open('./reports/unique.csv', 'w'))

setOfDescriptions = set()

for row in all_dataReader:
    if row[3] not in setOfDescriptions:
        entriesReader = csv.reader(open('./reports/all_data.csv', 'r'))
        amount = 0
        for entry in entriesReader:
            if row[3] == entry[3]:
                amount += 1
        setOfDescriptions.add(row[3])
        uniqueWriter.writerow([amount, row[1], row[2], row[3]])
