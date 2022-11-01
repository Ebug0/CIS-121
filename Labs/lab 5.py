"""
Ethan Livermore
Friday lab 9/23/2022
Cis 121
"""

#Your code goes here.



encodedWord = "EOUUUUOUU"
wused = False
#encodedWord = "WBLARF8TTS"
run = len(encodedWord)
print(encodedWord)
newstring = ""

for i in range (0,run):
	if encodedWord[i] == "L":
		newstring += "T"
	elif encodedWord[i] == "T":
		newstring += "L"
	elif encodedWord[i] == "8":
		newstring += "A"
	elif encodedWord[i] == "B":
		newstring += "A"
	elif encodedWord[i] == "A":
		newstring += "E"
	elif encodedWord[i] == "E":
		newstring += "B"
	elif wused == True:
		wused = False
	elif encodedWord[i] == "U":
		if wused == False:
			newstring += "W"
			wused = True
	else:
		newstring += encodedWord[i]
	
	#encodedWord = "WBLARF8TTS"
	#encodedWord = "L8KAOUL"
	#encodedWord = "E8N8N8"
	#encodedWord = "8TRA8DY T8LA"
	#encodedWord = "8TT LHA TILLTA LIMAS"	
	#encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	#encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
print(newstring)
	
	#encodedWord = "UUHO"  		#Used for Bonus
	#encodedWord = "EOUUUUOUU" 	#Used for Bonus











#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
