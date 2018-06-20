'''
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement
and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''
import math

distance = [0, 0]
while True:
	movement = input()
	if not movement:
		break
	movement = movement.split(" ")
	direction = movement[0]
	steps = int(movement[1])

	if direction == "RIGHT":
		distance[0] += steps
	elif direction == "LEFT":
		distance[0] -= steps
	elif direction == "UP":
		distance[1] += steps
	elif direction == "DOWN":
		distance[1] -= steps
print(round(math.sqrt((distance[0]*distance[0])+(distance[1]*distance[1]))))

