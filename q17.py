'''
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''
totalAmount =0
while True:
	
	trans = input("Enter Transaction in given format : ")
	if not trans:
		break;
	
	values = trans.split(" ")
	op = values[0]
	amount = int(values[1])

	if op == "D":
		totalAmount += amount
	elif op == "W":
		totalAmount -= amount
	else:
		pass

print(totalAmount)