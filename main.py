import utils
import sys

def main():
	attendFileName = sys.argv[1]
	statsFileName = sys.argv[2]
	attendData = utils.readCSV(attendFileName)
	statsData = utils.readCSV(statsFileName)

	for row in attendData:
		print(row)
	for row in statsData:
		print(row)



if __name__ == "__main__":
    main()