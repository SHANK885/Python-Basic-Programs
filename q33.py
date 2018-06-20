'''
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
'''

def dic(lower,upper):
	d = {}
	for i in range(lower,upper+1):
		d[i] = i*i
	print(d)

dic(1,20)
