### csvreader.py
# Version 1.0.0
#
# Opens a csv file and prints the contents. The user can specify a csv
#	to read in the command line, or if they don't it will default to
#	read '../Resources/Magic10Normal5Items.csv'
#
# Coded By:
# Graham MacDonald
# Kyle Hoffmann


import csv
import sys

# readCSVContents
#
# Opens a specified csv file and prints out its contents seperated by a " - "
def readCSVContents(readFileName):
	# Try to open the CSV and print its contents.
	with open(readFileName, newline='') as csvfile:
	    csvreader = csv.reader(csvfile, delimiter=',')
	    for row in csvreader:  
	        print(' -  '.join(row))

# Main for testing, This will allow the user to specify a test csv file.
def __main():
	# Define a default csv to open
	readFileName = '../Resources/Magic10Normal5Items.csv'

	# Checks if the user offered and argument, we assume that this is a csv
	if len(sys.argv) > 1:
		readFileName = sys.argv[1]

	# Call the csv reader itself. 
	readCSVContents(readFileName)


if __name__ == '__main__':
    __main()
