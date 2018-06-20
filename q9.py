'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

lines = []

while (1):
	sentence = input("Enter the Sentence: ")

	if sentence:
		lines.append(sentence)
	else:
		break

for line in lines:
	print(line.upper())
