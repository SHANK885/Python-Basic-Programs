'''
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

sen = input("Enter the sentence:")
dic = {"DIGITS":0,"LETTERS":0}
for character in sen:
	if character.isdigit():
		dic["DIGITS"] += 1
	elif character.isalpha():
		dic["LETTERS"] += 1
	else:
		pass
print("LETTERS ",dic["LETTERS"])
print("DIGITS",dic["DIGITS"])