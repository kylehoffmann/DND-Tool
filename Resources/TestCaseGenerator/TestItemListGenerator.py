# testItemListGenerator.py
#
# Generates a test file for the user, the specifics for test cases are defined in config.json
#
# Coded By:
# Kyle Hoffmann

import csv
import json
import os
import sys

# configFileValidateAndRepair
def generateTestFile(writeFileName):

	# Define the directory where the test files are to be saved.
	testFileDir = 'testFiles'

	# Open the Config File
	# Try to open the config file
	try:
		# Success - Save configs in a dictonary
		configFile = open('./config.json', 'r')
		cfData = json.load(configFile)
		configFile.close()

		# ToDo: Add a config file integrity check. I would suggest adding that to the ConfigFile.py functions.

	except OSError:
		# Falure - Inform the user to run the config tool and exit. 
		print("Config file missing" +
			"Please run ConfigTool.py")
		quit()

	#ToDo

	# Initalize a data structure to save the contents of the new file in
	tfData = []
	counter = 0

	try:
		# Open the list of items and save the number of items specified in Config.json {UsedNumberOfItems}
		with open(cfData["itemList"], newline='') as itemCSVFile:
			itemCSVreader = csv.reader(itemCSVFile, delimiter=',')
			for row in itemCSVreader: 
				#Stop recoding items once the item limit has been reached.
				if counter > cfData["UsedNumberOfItems"]:
					break

				# Append the header or item to the output file contents
				tfData.append(row)

				# Count the number of items recoreded. This will be the item number of the next item to be recorded
				counter += 1

		# ToDo: Add a setting and rework this action to choose items randomly up to the requried number specifed in Config.json (Also not implmented)

	except OSError:
		pass

	# Generate Repeated Items
	
	# Generate Columns with empty strings
	
	# Generate Empty rows, or entires that are a blank line
	
	# Generate Records missing columns 
	
	# Generate IDs that have values that arent a number
	
	# Generate IDs with a negative integer number
	
	# Generate IDs with a non-integer number
	
	# Generate Random words that arent Rarities set as a value
	
	# Generate Negative Integers set as a value
	
	# Generate Non-integer numbers set as a value

	# Save all the generated rows as a file.
	#		- ToDo: While writing a file there might be blank rows added depending on Config.Json {EmptyRows}
	# ToDo: Optionally randomize the order of records depnding on Config.json {RandomValues}

	# Check if the test file directory exists
	if not os.path.isdir('./' + testFileDir):
		os.mkdir(testFileDir)

	outputFile = open(testFileDir + "/" + writeFileName, "w")
	for row in tfData:
		# Make an empty string to print to a file
		record = ""

		# Creat a falue to check for the first cell in a row
		firstCell = True

		for cell in row:
			# Add a comma if this is not the first cell.
			if firstCell:
				firstCell = False
			else:
				record += ","

			# Add the current cell to the file output
			record += cell

		# Write a record in the output file
		outputFile.write(record + "\n")

	# Finish writing the file
	outputFile.close()




# Main function
#
# Runs the test file generator
def __main():
	# Define a default csv to ovewrite
	writeFileName = 'newTestFile.csv'

	# Checks if the user offered and argument, we assume that this is a csv
	if len(sys.argv) > 1:
		writeFileName = sys.argv[1]

	generateTestFile(writeFileName)


if __name__ == '__main__':
    __main()