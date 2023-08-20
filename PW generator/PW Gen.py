from ast import Num
from sre_parse import SPECIAL_CHARS
import random

#Read inputs from the user and convert Num_pass and Length into int variables for the later program
Num_pass = input("How many passwords do you need? ")
num_pass = int (Num_pass)
Length = input("How long does your password need to be? ")
length = int (Length)
char = input("Does your password require special characters? ")
random.choice

#If statements that finds if Specical characters are needed
if char == 'Y' or char == 'y':
	counter1 = 0
	while counter1 < num_pass:
		counter2 = 0
		while counter2 < length:
			pw = random.randint(33, 126)
			char_password = chr (pw)
			string_password = char_password
			counter2 += 1
			print (string_password , end="")
		counter1 += 1
		print("")

#Secondary else if statement for no special characters
elif char == 'n' or char == 'N':
	counter1 = 0
	while counter1 < num_pass:
		counter2 = 0
		while counter2 < length:
			for x in range(length):
				pw = choice([(48,57),(65,90),(97,122)])
				pw2 = randint(*pw)
				char_password = chr (pw2)
				string_password = char_password
			counter2 += 1
			print (string_password , end="")
		counter1 += 1
		print("")

#Final else statement for inputs that are not Y or N.
else:
	print ("Invalid input please select Y or N!")
