'''
Please write a program using generator to print 
the even numbers between 0 and n in
comma separated form while n is input by console.
'''

def printEven(number):
	i = 0 
	while i <= number:
		if i%2 == 0:
			yield i
		i+=1

n = int(input("Enter the value of N : "))
output = []
for i in printEven(n):
	output.append(str(i))
print(",".join(output))