'''
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
'''

def tupl(lower,upper):
	t = []
	for i in range(lower,upper+1):
		t.append(i)
	print(tuple(t))

tupl(1,20)