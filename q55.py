'''
Write a program which accepts a sequence of words 
separated by whitespace as input to print the words
composed of digits only.
'''
import re
seq = input("Enter the comma separated sequence of words: ")
print(re.findall("\d+",seq))

