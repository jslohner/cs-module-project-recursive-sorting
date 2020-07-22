# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
	# get mid point by adding start and end
	# then dividing them by 2
	mid = (start + end) // 2
	# if array is empty return -1
	if not arr:
		return -1
	# if mid point is equal to
	# target return mid index
	elif target == arr[mid]:
		return mid
	# if target is less than mid
	elif target < arr[mid]:
		# return binary_search function call passing
		# in the new end value with the existing data
		return binary_search(arr, target, start, mid - 1)
	# if target is greater than mid
	elif target > arr[mid]:
		# return binary_search function call passing
		# in the new start value with the existing data
		return binary_search(arr, target, mid + 1, end)
	# if target isn't found in array return -1
	return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
	start = 0
	end = len(arr) - 1
	while start <= end:
		mid = (start + end) // 2
		if not arr:
			return -1
		elif arr[0] < arr[-1]:
			if target == arr[mid]:
				return mid
			elif target < arr[mid]:
				end = mid - 1
			elif target > arr[mid]:
				start = mid + 1
		elif arr[0] > arr[-1]:
			if target == arr[mid]:
				return mid
			elif target < arr[mid]:
				start = mid + 1
			elif target > arr[mid]:
				end = mid - 1
	return -1
