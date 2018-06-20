'''
Please write a binary search function which searches
an item in a sorted list. The function should return
the index of element to be searched in the list.
'''
import math

def binarySearch(lis, element):
	left = 0
	right = len(lis)-1
	index = -1

	while right >= left and index == -1:

		mid = int(math.floor((right+left)/2.0))
		if lis[mid] == element:
			index = mid
		elif lis[mid] < element:
			left = mid+1
		else:
			right = mid-1

	return index

li = [2,5,7,11,17,222]
ind = binarySearch(li,11)
print(ind)
