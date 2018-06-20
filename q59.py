'''
f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).
'''

def fun(n):
	if n == 0:
		return 0
	else:
		return fun(n-1) + 100

n = int(input("Enter The Value of N : "))
print(fun(n))