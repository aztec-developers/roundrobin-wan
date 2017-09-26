import csv

def readCSV(filename):
	rows = []
	with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
    	rows.append(row)
  return rows
  