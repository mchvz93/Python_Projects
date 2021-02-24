def bubblesort(lst):
	for i in range (len(lst)-1):
		for j in range (len(lst)-1):
			if (lst[j]>lst[j+1]):
				t = lst[j]
				lst[j] = lst[j+1]
				lst[j+1] = t
	return lst

def BinarySearch(lst, key):
	low = 0
	high = len(lst)-1
	while high>= low:
		mid = (low + high)//2
		if key < lst[mid]:
			high = mid -1
		elif key == lst[mid]:
			return 'found'
		else:
			low = mid + 1
	return 'Not found'

def main():
    lst1 = [11, 4, 7, 10, 2, 45, 66, 28]
    lst = bubblesort(lst1)
    print(BinarySearch(lst,11))

main()
