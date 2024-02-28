import random, time

# lets start by filling an array of n size with random numbers 1-999
# usage: declare an array and pass the size of the array 
def fill_array(n):
        return [random.randint(1, 999) for _ in range(n)]

#lets create a function to display the first five elemetns in the array, this is used for testing
def first_five(arr):
      for i in range(min(5, len(arr))):
        print(arr[i])

# we will use this for the best case of quick sort
# we divide the list in half
def best_partition(arr, low, high):
    # Choose the middle element as pivot and swap it with the last element
    middle = (low + high) // 2
    arr[middle], arr[high] = arr[high], arr[middle]
    
    pivot = arr[high]  # Now, the pivot is the middle element, but placed at the end.
    i = (low - 1)  # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# quick sort function for testing quick sort in its best case.
def best_quickSort(arr, low, high):
    if low < high:
        # Partition the array into two halves
        pivotIndex = best_partition(arr, low, high)

        # Recursively sort each half
        quickSort(arr, low, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, high)

# partition used for quick sort
def partition(arr, low, high):
    
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# quick sort function
def quickSort(arr, low, high):
    while low < high:
        pivotIndex = partition(arr, low, high)

        # Recursively call the smaller partition
        # Then loop back to sort the other part iteratively to reduce maximum recursion depth
        if pivotIndex - low < high - pivotIndex:
            quickSort(arr, low, pivotIndex - 1)
            low = pivotIndex + 1
        else:
            quickSort(arr, pivotIndex + 1, high)
            high = pivotIndex - 1

# dr hu code for bubble sort
def bubbleSort(myList): # Bubble Sort Algorithm
    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j+1] = \
                           myList[j + 1], myList[j]
    return myList


# dr hu code for merge sort
def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

# shell sort algorithm
def shell_sort(arr):
    n = len(arr)
    # Start with a large gap, then reduce the gap
    gap = n // 2
    while gap > 0:
        # Do a gapped insertion sort for this gap size.
        # The first gap elements arr[0:gap-1] are already in gapped order
        # Keep adding one more element until the entire array is gap sorted
        for i in range(gap, n):
            # Save arr[i] in temp and make a hole at position i
            temp = arr[i]
            # Shift earlier gap-sorted elements up until the correct
            # location for arr[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            # Put temp (the original arr[i]) in its correct location
            arr[j] = temp
        gap //= 2

