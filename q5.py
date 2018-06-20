'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class STRING:

	def  __init__(self):
		self.str = ""

	def getString(self):
		self.str = input("Enter the String:")

	def printString(self):
		print(self.str.upper())


test = STRING()
test.getString()
test.printString()