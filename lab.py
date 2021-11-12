import ssl
import csv
import json
#number 1
sales_data = []

file = "SalesJan2009.csv"
inputFile = open(file, "r")
dataDict = {}
#number 2
print("Creating JSON file..")
with open(file) as inputFile:
    csvReader = csv.reader(inputFile)
    for r in csvReader:    
#number 3
        sales_data.append(r)
#number 4
with open("transaction_data.json", 'w') as output: 
    jsonFile = json.dumps(sales_data,indent=4)
    output.write(jsonFile)
print("Done!")