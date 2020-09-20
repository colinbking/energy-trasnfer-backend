import csv
import math
import datetime
from datetime import datetime

mapping = {}
dates = []

def readRow(row):

    custID = int(row[0])
    c3 = math.inf if row[4] == '-' else math.ceil(int(row[4])/30000)
    c4 = math.inf if row[5] == '-' else math.ceil(int(row[5])/30000)
    loadTime = min(c3, c4)
    mapping[custID] = loadTime
    start = row[6] + "20"
    end = row[7] + "20"
    dateStart = datetime.strptime(start, "%m/%d/%Y")
    dateEnd = datetime.strptime(end, "%m/%d/%Y")
    dates.append((custID, dateStart, dateEnd))

def readfile():
    with open('energyTransfer.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar="|")
        headers = next(reader, None)
        for row in reader:
            readRow(row)
    return mapping, dates
