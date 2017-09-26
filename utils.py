import csv
import urllib.request
def readCSV(filename):
	rows = []
	with open(filename) as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			rows.append(row)
	return rows


def getGitHubStats(username):
	urllib.request.urlopen("http://example.com/foo/bar").read()