import utils
import sys
from person import Person

def main():
	attendFileName = sys.argv[1]
	statsFileName = sys.argv[2]
	attendData = utils.readCSV(attendFileName)
	statsData = utils.readCSV(statsFileName)

	people = {}
	for row in statsData:
		p = Person(row)
		people[p.name] = p

	for row in attendData:
		if row[1] == 'yes':
			print(people[row[0]].str())
	



if __name__ == "__main__":
    main()