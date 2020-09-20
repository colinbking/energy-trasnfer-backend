import csv
import math
import 

mapping = {}
def readRow(row):
    custID = int(row[0])
    print(custID)
    c3 = 0 if row[4] == '-' else math.ceil(int(row[4])/30000)
    c4 = 0 if row[5] == '-' else math.ceil(int(row[5])/30000)
    loadTime = min(row[4], row[5])
    print(loadTime)
    mapping[custID] = loadTime

with open('energyTransfer.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar="|")
    headers = next(reader, None)
    for row in reader:
        readRow(row)

print(mapping)
