import csv
import os

######### Core functions #########

def initFile(fileName, headers=[], data=[]):
    if not fileExist(fileName):
        with open('./storage/'+fileName+'.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    else:
        existingColumns = getColumns(fileName)
        missingColumns = [h for h in headers if h not in existingColumns]
        if missingColumns:
            existingData = readFile(fileName)
            newHeaders = existingColumns + missingColumns
            for row in existingData:
                for col in missingColumns:
                    row[col] = ""
            with open('./storage/'+fileName+'.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=newHeaders)
                writer.writeheader()
                for row in existingData:
                    writer.writerow(row)

def fileExist(fileName):
    return os.path.isfile('./storage/' + fileName + '.csv')

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
        fieldnames = getColumns(fileName)
        try:
            with open('./storage/'+fileName+'.csv', 'w', encoding="utf-8", newline='') as csvfile:
                csv_dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                csv_dict_writer.writeheader()
                for row in data:
                    csv_dict_writer.writerow(row)
                    print(f"writing ${row}")
        except Exception as e:
            print("error while wr", e)

def getColumns(fileName):
    if (fileExist(fileName)):
        with open('./storage/'+fileName+'.csv') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                return row # returns the first row of the table, the headers
            return []


######### Usable functions #########

# This function returns the row that is matching with the given key-value :
# getData('test', [key, value])
def getData(fileName, findKeys):
    keyName, keyValue = findKeys[0], findKeys[1]
    if (fileExist(fileName)):
        data = readFile(fileName)
        for row in data:
            if (row[keyName] == keyValue):
                return row


# This function updates the row to the new given value :
# setData('test', [key, value], {...})
def updateData(fileName, findKeys, newRow):
    keyName, keyValue = findKeys[0], findKeys[1]
    if (fileExist(fileName)):
        data = readFile(fileName)
        for i in range(len(data)):
            if (data[i][keyName] == keyValue):
                data[i] = newRow
                break
        writeFile(fileName, data)

# Similar to the previous function, but adds the row if the row is not already found :
# setData('test', [key, value], {...})
def upsertData(fileName, findKeys, newRow):
    keyName, keyValue = findKeys[0], findKeys[1]
    if (fileExist(fileName)):
        data = readFile(fileName)
        found = False
        for i in range(len(data)):
            if (data[i][keyName] == keyValue):
                data[i] = newRow
                found = True
                break
        if found:
            try:
                writeFile(fileName, data)
            except Exception as e:
                print("error while writing:", e)
        else:
            insertData(fileName, newRow)


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