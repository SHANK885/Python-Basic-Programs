'''
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
'''
def lis(lower,upper):
	l = []
	for i in range(lower,upper+1):
		l.append(i)
	print(l)

lis(1,20)