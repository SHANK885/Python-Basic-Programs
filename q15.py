'''
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''

num = input("Enter the Digit : ")

out = 0
i = 1
string = num
while i <= 4:
	out += int(string) 
	string += num 
	i += 1
print(out)
