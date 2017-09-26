import csv
import urllib.request
import json

def readCSV(filename):
	rows = []
	with open(filename) as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			rows.append(row)
	return rows


def getGitHubStats(username):
	response = urllib.request.urlopen("https://api.github.com/users/aztec-developers/repos")
	data = json.load(response) 
	for el in data:
		print(el['name'])
		response = urllib.request.urlopen("https://api.github.com/repos/aztec-developers/"+el["name"]+"/stats/contributors")
		contributors = json.load(response)
		for con in contributors:
			print("-"+con['author']['login'] +" "+ str(con['total']))
		
	