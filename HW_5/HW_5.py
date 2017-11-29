import argparse
import os
import logging
import urllib.request as urllib2
import json
from datetime import datetime as DT
import csv
import re

import config as cfg

file_path = cfg.folder
directory = os.path.dirname(file_path)

if not os.path.exists(directory):
    os.makedirs(directory)

logger = logging.getLogger('HW_5')
logger.setLevel(logging.INFO)

fh = logging.FileHandler(cfg.folder + 'hn_parser.log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - ' +
    '%(message)s')
fh.setFormatter(formatter)
# add handler to logger object
logger.addHandler(fh)
logger.info('Program started')

parser = argparse.ArgumentParser()
parser.add_argument('-c', default=cfg.defaultCategory,
    choices=cfg.availableCategories)

try:
    url = cfg.urlList + parser.parse_args().c + '.json?print=pretty'
    response = urllib2.urlopen(url, timeout=5)
    responseData = json.loads(response.read().decode('utf-8'))
    logger.info('Category: getting response to url: ' + url)
except Exception as e:
    logger.error(e)

listOfRecords = []

for dataRecord in responseData:
    try:
        url = cfg.urlRecord + str(dataRecord) + '.json?print=pretty'
        response = urllib2.urlopen(url, timeout=5)
        record = json.loads(response.read().decode('utf-8'))
        listOfRecords.append(record)
        logger.info('Record: getting response to url: ' + url)
    except Exception as e:
        logger.error(e)

sortedList = []
dateFilter = DT.strptime(cfg.filterFromDate, '%Y-%m-%d').timestamp()

for i in listOfRecords:
    if i.get('time') >= dateFilter and i.get('score') >= cfg.filterScore:
        sortedList.append(i)

listOfRecords = sortedList
regex = '\<\w.*\<\/\w\>'

try:
    for record in listOfRecords:
        convertDate = DT.fromtimestamp(record.get('time')).strftime('%Y-%m-%d %H:%M:%S')
        text = str(record.get('text'))
        textWithoutTags = re.sub(regex, '', text)
        with open(cfg.folder + cfg.reportFile, 'a') as csvFile:
            csvWrite = csv.writer(csvFile)
            csvWrite.writerow([record.get('by'), record.get('id'),
            record.get('score'), textWithoutTags, convertDate,
            record.get('title'), record.get('type'), record.get('url')])
    logger.info('The records is written to the file')
except Exception as e:
    logger.error(e)

logger.info('The program has completed!')
