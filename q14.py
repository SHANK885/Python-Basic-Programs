'''
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
sen = input("Enter the sentence:")
dic = {"UPPER CASE":0,"LOWER CASE":0}
for character in sen:
	if character.isupper():
		dic["UPPER CASE"] += 1
	elif character.islower():
		dic["LOWER CASE"] += 1
	else:
		pass
print("UPPER CASE",dic["UPPER CASE"])
print("LOWER",dic["LOWER CASE"])
