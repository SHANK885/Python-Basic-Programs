'''
Please write a program which count and print the numbers of each
character in a string input by console.
'''

dic = {}
string = input()

for s in string:
	dic[s] = dic.get(s,0)+1

print("\n".join(['%s,%s' % (k, v) for k, v in dic.items()]))