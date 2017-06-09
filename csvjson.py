import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + '' + str(row))
#This is just iterating through each row.

import csv
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writernow(['spam', 'eggs', 'bacon', 'ham'])
