import csv, os

os.makedirs('headerRemoved', exist_ok=True)
#This is making a directory for the newly copied and fixed csvs to go into once completed.

#Loop through every file in the current working directory.

for csvFile in os.listdir('.'):
    #This is for determing which have file extensions of csv and which don't.
    if not csvFile.endswith('.csv'):
        continue #Skip non-csv files.
    print('Removing header from' + csvFile + '...')

    #TODO: Read the CSV file in (skipipng first row).
    csvRows = []
    csvFileObj = open(csvFile)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        #If you are currently reading row 1, than skip it and append each row following to the new list.
        csvRows.append(row)
    csvFileObj.close()

    #TODO Write out the CSV File.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    #The new line is just to get around double spacing, to single spaced lines in csv / excel view.
    csvWriter = csv.writer(csvFileObj)
    #The CSV writer object will write the list to a CSV file in headerRemoved using Csv Filename. This will ovewrite the original file.
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
