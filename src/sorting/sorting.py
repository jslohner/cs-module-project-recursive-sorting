# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
	elements = len(arrA) + len(arrB)
	merged_arr = [0] * elements
	# my original solution
	# loop through each element index
	for i in range(elements):
		# check if both arrays have elements
		if (arrA) and (arrB):
			# if arrA[0] < arrB[0]
			if arrA[0] < arrB[0]:
				# set merged_arr at current
				# index to first element of arrA
				merged_arr[i] = arrA[0]
				# remove first element of arrA
				arrA.pop(0)
			# if arrA[0] > arrB[0]
			elif arrA[0] > arrB[0]:
				# set merged_arr at current
				# index to first element of arrB
				merged_arr[i] = arrB[0]
				# remove first element of arrB
				arrB.pop(0)
		# check if arrA has elements and arrB doesn't
		elif (arrA) and (not arrB):
			# set merged_arr at current
			# index to first element of arrA
			merged_arr[i] = arrA[0]
			# remove first element of arrA
			arrA.pop(0)
		# check if arrB has elements and arrA doesn't
		elif (not arrA) and (arrB):
			# set merged_arr at current
			# index to first element of arrB
			merged_arr[i] = arrB[0]
			# remove first element of arrB
			arrB.pop(0)
	# return merged array
	return merged_arr

	# while loop with pointer solution
	# merged_arr = []
	# a = 0
	# b = 0
	# while (a < len(arrA)) and (b < len(arrB)):
	# 	if arrA[a] < arrB[b]:
	# 		merged_arr.append(arrA[a])
	# 		a += 1
	# 	else:
	# 		merged_arr.append(arrB[b])
	# 		b += 1
	#
	# if a < len(arrA):
	# 	merged_arr.extend(arrA[a:])
	# elif b < len(arrB):
	# 	merged_arr.extend(arrB[b:])
	#
	# return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
	# check if array length is greater than 1
	if len(arr) > 1:
		# get mid point by dividing length of array by 2
		mid = len(arr) // 2
		# call merge_sort fn on left side of array
		arrA = merge_sort(arr[:mid])
		# call merge_sort fn on right side of array
		arrB = merge_sort(arr[mid:])
		# merge the two arrays and assign the return value to arr variable
		arr = merge(arrA, arrB)
	# return array
	return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
	start2 = mid + 1
	if (arr[mid] < arr[start2]):
		return
	while ((start <= mid) and (start2 <= end)):
		if (arr[start] <= arr[start2]):
			start += 1
		else:
			value = arr[start2]
			index = start2
			while (index != start):
				arr[index] = arr[index - 1]
				index -= 1
			arr[start] = value
			start += 1
			mid += 1
			start2 += 1

def merge_sort_in_place(arr, l, r):
	if (l < r):
		m = l + (r - l) // 2
		merge_sort_in_place(arr, l, m)
		merge_sort_in_place(arr, (m + 1), r)
		merge_in_place(arr, l, m, r)
