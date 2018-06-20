tp = (1,2,3,4,5,6,7,8,9,10)
lis = []

for i in tp:
	if i%2 == 0:
		lis.append(i)
tp_new = tuple(lis)
print(tp_new)
