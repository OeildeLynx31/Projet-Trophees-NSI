import csv
import os

######### Core functions #########

def initFile(fileName, headers=[]):
    if (not fileExist(fileName)):
        with open('./storage/'+fileName+'.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()

def fileExist(fileName):
    if os.path.isfile('./storage/'+fileName+'.csv'):
        return True
    return False

def readFile(fileName):
    if (fileExist(fileName)):
        with open('./storage/'+fileName+'.csv', newline='') as csvfile:
            dictReader = csv.DictReader(csvfile)
            rowArray = []
            for row in dictReader:
                rowArray.append(row)
            return rowArray

def writeFile(fileName, data):
    if (fileExist(fileName)):
        fieldnames = getColumns(fileName, data)
        with open('./storage/'+fileName+'.csv', 'w', encoding="utf-8", newline="") as csv_file:
            csv_dict_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_dict_writer.writeheader()
            for line in data:
                csv_dict_writer.writerow(line)

def getColumns(fileName):
    if (fileExist(fileName)):
        with open('./storage/'+fileName+'.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                return row # returns the first row of the table, the headers
            return []


######### Usable functions #########

# This function returns the row that is matching with the given key-value :
# getData('test', [key, value])
def getData(fileName, findKeys):
    keyName, keyValue = findKeys[0], findKeys[1]
    if (fileExist(fileName)):
        rowList = readFile(fileName)
        for row in rowList:
            if (row[keyName] == keyValue):
                return row


# This function updates the row to the new given value :
# setData('test', [key, value], {...})
def updateData(fileName, findKeys, newRow):
    keyName, keyValue = findKeys[0], findKeys[1]
    if (fileExist(fileName)):
        data = readFile(fileName)
        for row in data:
            if (row[keyName] == keyValue):
                row = newRow
                break
        writeFile(fileName, data)


# Similar to the previous function, but adds the row if the row is not already found :
# setData('test', [key, value], {...})
def upsertData(fileName, findKeys, newRow):
    keyName, keyValue = findKeys[0], findKeys[1]
    if (fileExist(fileName)):
        data = readFile(fileName)
        found = False
        for row in data:
            if (row[keyName] == keyValue):
                row = newRow
                found = True
                break
        if found:
            writeFile(fileName, data)
        else:
            addData(fileName)


# This function adds a new row to the table :
# addData('test', {...})
def insertData(fileName, row):
    if (fileExist(fileName)):
        data = readFile(fileName)
        data.append(row)
        writeFile(fileName, data)


# This function removes the matching row from the table :
# remData('test', [key, value])
def removeData(fileName, findKeys):
    keyName, keyValue = findKeys[0], findKeys[1]
    if (fileExist(fileName)):
        data = readFile(fileName)
        newData = []
        for row in data:
            if (row[keyName] != keyValue):
                newData.append(row)
                break
        writeFile(fileName, newData)