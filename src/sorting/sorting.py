# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
	elements = len(arrA) + len(arrB)
	merged_arr = [0] * elements
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
	# Your code here
	return

def merge_sort_in_place(arr, l, r):
	# Your code here
	return
