'''
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
 Then the function needs to print the last 5 elements in the list.
'''

def lis(lower,upper):
	l = []
	for i in range(lower,upper+1):
		l.append(i)
	print(l[-5:])

lis(1,20)