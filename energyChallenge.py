import csv
import math
import datetime

mapping = {}
dates = []
def readRow(row):
    custID = int(row[0])
    c3 = math.inf if row[4] == '-' else math.ceil(int(row[4])/30000)
    c4 = math.inf if row[5] == '-' else math.ceil(int(row[5])/30000)
    loadTime = min(c3, c4)
    mapping[custID] = loadTime
    start = row[6]
    end = row[7]
    print(start)
    print(reorderDate(start))

def reorderDate(date):
    newDate = "20"
    curr = 0
    start = 0
    while(curr < len(date)):
        
        curr = curr + 1
        if(date[len(date)-curr] == '/'):
            newDate = newDate + date[len(date)-curr+1:len(date)-start]
            start = curr
            newDate = newDate + '-'
    return newDate


with open('energyTransfer.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar="|")
    headers = next(reader, None)
    for row in reader:
        readRow(row)
