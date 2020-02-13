#Input: The party ID(int), the name(string), description(string) and value in copper(int)
#Return: Single dictionary containg the partys
#Function: Creates a default party with essential parameters for limited testing
def PartyInit(ID, name):
	partyDic = {}
	partyDic["ID"] = ID
	partyDic["name"] = name  
	return partyDic


#Input: Dictionary containing full party details
#Return: Single dictinary containg values for a default party
#Function: Creates a default party with essential parameters for limited testing
def DefaultID():
	ID = 1
	name = "Maverick minotaurs"
	return PartyInit(ID, name)

#Input: Dictionary containing full party details
#Return: Returns party ID as an int
#Function: When called with an party dictonary gives the party's ID
def GetID(party):
	return party["ID"]

#Input: Dictionary containing full party details
#Return: Nothing
#Function: Prints all party traits to cmd with formatting
def FullpartyPrint (party):
	for traits in party:
		print(traits + ":", party[traits])

#Input: Dictionary containing full party details
#Return: Nothing
#Function: Sends request for party detail print including ID and name
def IDPrint (party):
	traits = ["ID","name"]
	PartialpartyPrint(party, traits)

#Input: Dictionary containing full party details + array with traits to be printed
#Return: Nothing
#Function: Prints traits listed in the passed array
def PartialpartyPrint (party, traits):
	for trait in traits:
		print(trait + ":", party[trait])

#starting function only runs if program is run independently
def __main():
	party = DefaultID()
	FullpartyPrint(party)
	print("")
	IDPrint(party)
	print("")
	print(GetID(party))


if __name__ == '__main__':
    __main()





