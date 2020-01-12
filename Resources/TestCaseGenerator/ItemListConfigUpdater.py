# ItemListConfigUpdater
# Version 1.0.0
#
# Reads an Item List included with the Test Case generator to retreive the number of items
#	stored in the file. This value is then updated in the config.json file.
# This program will generate a configfile if it is missing, but it will use the default 
#	"./ItemList.csv" as the item list location if it has to do so.
# In the current form it doesn't validate the items in the list are real items, it expects a valid list.
#
# Coded By:
# Kyle Hoffmann

import csv
import sys
import json

# itemListConfigUpdater( Name of the file to be used as an item list )
#
# Takes the name of an item file name, then counts the number of items and
#	updates the config file with a number of items and the new item file name.
def itemListConfigUpdater(readFileName):
	# Initlaize Valiables
	lineCount = 0

	if (readFileName == ""):
		# Make a default configFile
		cfData = { "itemList":"./ItemList.csv" }

		# Try to open an existing config file
		try:
			#If file exists overwrite the default config file.
			configFile = open('./config.json', 'r')
			cfData = json.load(configFile)
		except OSError:
			# Open file failed, inform the user and exit the program.
		    pass
			

		# Prints the name of the item list csv in the config file. For testing.
		# print(cfData["itemList"])

		# Set using a the config file data
		readFileName = cfData["itemList"]

	else:
		cfData = { "itemList":readFileName }

	# Attempt to open specified file.
	try:
	    itemFile = open(readFileName, 'r')
	except OSError:
		# Open file failed, inform the user and exit the program.
	    print("Could not open/read file:", readFileName)
	    sys.exit()

	# File Exists open and do stuff.
	with itemFile:

		# Loop though line in the file
	    reader = csv.reader(itemFile)
	    for row in reader:
	    	# Count the number of items in the file.
	        lineCount += 1

	# Print the number of lines. For testing.
	# print(lineCount)

	# Update the config Files item count
	cfData["MaxNumberOfItems"] = lineCount

	# Save the updated ConfigFile
	with open('config.json', 'w') as fp:
	    json.dump(cfData, fp, indent=4)

	# Inform the user that program was sucessful
	print("Item list Update successful\n"\
		"Max items updated to", lineCount, "\n")


# Main function
#
# Looks for a user defined list of items to use. hands an empty string forward if none is found.
#	It calls the real function that updates the confige file with the item list's info.
def __main():

	# Initlaize an the readfile to have no name.
	readFileName = ""

	# Allows the user to specify a filename when the application is called.
	if len(sys.argv) > 1:
		readFileName = sys.argv[1]

	itemListConfigUpdater(readFileName)


if __name__ == '__main__':
    __main()
