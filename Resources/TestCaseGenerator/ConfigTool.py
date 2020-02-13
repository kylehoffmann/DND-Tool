# ConfigTool.py
#
# Opens the config file and repairs any missing parts of it.
#
# Coded By:
# Kyle Hoffmann

import ItemListConfigUpdater as ILCU
import json

# configFileValidateAndRepair
def configFileValidateAndRepair():

	# Validate and update the ItemList part of the config file.
	#	This will also insure that a config file is generated.
	ILCU.itemListConfigUpdater("")

	# Make a default configFile
	cfData = {}

	# Try to open an existing config file
	try:
		#If file exists overwrite the default config file.
		configFile = open('./config.json', 'r')
		cfData = json.load(configFile)
	except OSError:
		# Open file failed, inform the user and generate the new file.
		print("Config file was missing\n" +
			"Generating a new file.")

	# Add all the types of garbage the user could want
	cfData["DuplicateItems"] = 0		# Number of repeated Items
	cfData["EmptyColumns"] = "No"		# Columns with empty strings
	cfData["EmptyRows"] = 0				# Empty rows, or entires that are a blank line
	cfData["MissingColumns"] = "No"		# Records missing columns 
	cfData["NonNumberIDs"] = 0			# IDs that have values that arent a number
	cfData["NegNumberIDs"] = 0			# IDs with a negative integer number
	cfData["NonIntNumberIDs"] = 0		# IDs with a non-integer number
	cfData["FakeRarities"] = "No"		# Random words that arent Rarities set as a value
	cfData["NegativeValues"] = 0		# Negative Integers set as a value
	cfData["NonIntValues"] = 0			# Non-integer numbers set as a value
	cfData["RandomValues"] = "No"		# Randomize the test element order in the test files
	
	# Print the new contents of the config file. For Testing
	# print(cfData)

	# Save the updated ConfigFile
	with open('config.json', 'w') as configFile:
		json.dump(cfData, configFile, indent=4)


# Main function
#
# Runs the config file checker
def __main():

	configFileValidateAndRepair()


if __name__ == '__main__':
	__main()
