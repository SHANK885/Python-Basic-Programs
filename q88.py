'''
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits
in a farm. How many rabbits and how many chickens do we have?
'''
def howMany(heads, legs):
	noSolution = "!! NO SOLUTION !!"
	for i in range(heads+1):
		j = heads - i
		if (2*i) + (4*j) == legs:
			return i,j
		else:
			pass




heads = 35
legs = 94
sol = howMany(heads, legs)
print("Rabbits : ",sol[1], "\nChickens : ",sol[0])