'''
Please write a program using generator to print 
the numbers which can be divisible by 5 and 7 between 0 and n in 
comma separated form while n is input by console.
'''

def isDivisibleBY_5_7(number):
	i = 0 
	while i <= number:
		if i%5 == 0 and i%7 == 0:
			yield i
		i+=5

n = int(input("Enter the value of N : "))
output = []
for i in isDivisibleBY_5_7(n):
	output.append(str(i))
print(",".join(output))