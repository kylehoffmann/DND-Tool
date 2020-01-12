# ConfigTool.py
#
# Opens the config file and repairs any missing parts of it.
#
# Coded By:
# Kyle Hoffmann

import ItemListConfigUpdater as ILCU

# configFileValidateAndRepair
def configFileValidateAndRepair():

	# Validate and update the ItemList part of the config file.
	#	This will also insure that a config file is generated.
	ILCU.itemListConfigUpdater("")


# Main function
#
# Runs the config file checker
def __main():

	configFileValidateAndRepair()
	ILCU.main()


if __name__ == '__main__':
    __main()
