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
import random

def insertRecordInNewFileData(fileData, newRecord, Randomize):
	if Randomize.lower() == "no" or Randomize.lower() == "n":
		# If the goal isn't to randomize append data
		fileData.append(newRecord)
	else:
		#Choose a random place in the current file data and add the record there
		insertIndex = random.randrange(1, len(fileData)+1)
		fileData.insert(insertIndex, newRecord)



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
				if counter == 0:
					# The first row is the column headers, it should always be this way
					# ToDo: Add a config to allow violation of this.
					tfData.append(row)
				else:
					# Add the rest of the files sequentially or randomly based on the config file.
					insertRecordInNewFileData(tfData, row, cfData["RandomValues"])

				# Count the number of items recoreded. This will be the item number of the next item to be recorded
				counter += 1

		# ToDo: Add a setting and rework this action to choose items randomly up to the requried number specifed in Config.json (Also not implmented)

	except OSError:
		pass

	# Generate Repeated Items the config says to. This should go immendiately 
	#	after the valid items have been loaded and before anything else is added to the file. 
	if (isinstance(cfData["DuplicateItems"], int) and cfData["DuplicateItems"] > 0):

		# Generate the number of items the config file says to
		for i in range(0, cfData["DuplicateItems"]):
			# choose a random item to duplicate. This can pick the same item multiple times.
			duplicateIndex = random.randrange(1, len(tfData))
			insertRecordInNewFileData(tfData, tfData[duplicateIndex], cfData["RandomValues"])

	# Find a free starting item index. 
	# 		- This assumes that the input file is using the lowest sequential ids. It also adds space for duplicate items and empty rows.
	startingIndex = 1
	if isinstance(cfData["MaxNumberOfItems"], int):
		startingIndex += cfData["MaxNumberOfItems"]
	if isinstance(cfData["DuplicateItems"], int):
		startingIndex += cfData["DuplicateItems"]
	if isinstance(cfData["EmptyRows"], int):
		startingIndex += cfData["EmptyRows"]

	# Generate entries with empty coulmns if config says to
	if (cfData["EmptyColumns"].lower() == "yes" or cfData["EmptyColumns"].lower() == "y" ):

		# Loop through every possible combination of empty columns.
		#		- using modulus and divison the iteration number is used to toggle writing on the column.
		for i in range(0, 2**len(tfData[0])):
			# Initalize the new entry
			emptyColumnEntry = []

			# Add ID (or not)
			if i % 2 == 0:
				emptyColumnEntry.append(str(i + startingIndex))
			else:
				emptyColumnEntry.append("")
			
			# Add an item name (or not)
			if int(i / 2) % 2 == 0:
				emptyColumnEntry.append("EC Name - " + str(i))
			else:
				emptyColumnEntry.append("")

			# Add an item discription (or not)
			if int(i / 4) % 2 == 0:
				emptyColumnEntry.append("EC Discription - " + str(i))
			else:
				emptyColumnEntry.append("")

			# Add an item value (or not)
			if int(i / 8) % 2 == 0:
				emptyColumnEntry.append(str(i))
			else:
				emptyColumnEntry.append("")

			# Add the generated entry
			insertRecordInNewFileData(tfData, emptyColumnEntry, cfData["RandomValues"])

	
	# Generate Empty rows, or entires that are a blank line
	if (isinstance(cfData["EmptyRows"], int) and cfData["EmptyRows"] > 0):

		# Generate the number of empty columns the config file says to
		for i in range(0, cfData["EmptyRows"]):
			# Save an empty row.
			insertRecordInNewFileData(tfData, [], cfData["RandomValues"])
	
	# Update the starting index
	startingIndex += 2**len(tfData[0])
	
	# Generate Records missing columns  if config says to
	if (cfData["MissingColumns"].lower() == "yes" or cfData["MissingColumns"].lower() == "y" ):

		# Loop through every possible combination of missing columns.
		#		- using modulus and divison the iteration number is used to toggle writing on the column.
		for i in range(0, 2**len(tfData[0])):
			# Initalize the new entry
			emptyColumnEntry = []

			# Add ID (or not)
			if i % 2 == 0:
				emptyColumnEntry.append(str(i + startingIndex))
			
			# Add an item name (or not)
			if int(i / 2) % 2 == 0:
				emptyColumnEntry.append("MC Name - " + str(i))

			# Add an item discription (or not)
			if int(i / 4) % 2 == 0:
				emptyColumnEntry.append("MC Discription - " + str(i))

			# Add an item value (or not)
			if int(i / 8) % 2 == 0:
				emptyColumnEntry.append(str(i))

			# Add the generated entry
			insertRecordInNewFileData(tfData, emptyColumnEntry, cfData["RandomValues"])

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