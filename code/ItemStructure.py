import sys



#Input: The item ID(int), the name(string), description(string) and value in copper(int)
#Return: Single dictionary containg the items
#Function: Creates a default item with essential parameters for limited testing
def ItemInit(ID, name, desc, value):
	itemDic = {}
	itemDic["ID"] = ID 
	itemDic["name"] = name
	itemDic["desc"] = desc 
	itemDic["value"] = value
	return itemDic


#Input: Dictionary containing full item details
#Return: Single dictinary containg values for a default item
#Function: Creates a default item with essential parameters for limited testing
def DefaultID():
	ID = 1
	name = "Gnrglbrsh"
	desc = "Made by Goblins DC15 Con save to avoid 1d4 rounds of incapcatiation from vomiting. Goblins eh? "
	value = 1
	return ItemInit(ID, name, desc, value)

#Input: Dictionary containing full item details
#Return: Nothing
#Function: Prints all item traits to cmd with formatting
def FullItemPrint (item):
	for traits in item:
		print(traits + ":", item[traits])

#Input: Dictionary containing full item details
#Return: Nothing
#Function: Sends request for item detail print including ID and name
def IDPrint (item):
	traits = ["ID","name"]
	PartialItemPrint(item, traits)

#Input: Dictionary containing full item details + array with traits to be printed
#Return: Nothing
#Function: Prints traits listed in the passed array
def PartialItemPrint (item, traits):
	for trait in traits:
		print(trait + ":", item[trait])

#starting function
while True:
	item = DefaultID()
	#FullItemPrint(item)
	IDPrint(item)
	break





