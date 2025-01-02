# Quick Sort
# Quick sort is an efficient sorting algorithm that's widely used in production sorting implementations. Like merge sort, quick sort is a recursive divide and conquer algorithm.

# Divide:

# Select a pivot element that will preferably end up close to the center of the sorted pack
# Move everything onto the "greater than" or "less than" side of the pivot
# The pivot is now in its final position
# Recursively repeat the operation on both sides of the pivot
# Conquer:

# The array is sorted after all elements have been through the pivot operation

# explain_quick_sort = ""https://youtu.be/IpazwWu__Io""

# Algorithm
# Complete the quick_sort and partition functions according to the given algorithms.

# Note: The process is started with quick_sort(A, 0, len(A)-1).

# quick_sort(nums, low, high):

# If low is less than high:
# Partition the input list using the partition function
# Recursively call quick_sort on the left side of the partition
# Recursively call quick_sort on the right side of the partition
# partition(nums, low, high):

# Set pivot to the element at index high
# Set i to low
# For each index (j) from low to high
# If the element at index j is less than the pivot:
# Swap the element at index i with the element at index j
# Increment i by 1
# Swap the element at index i with the element at index high
# Return the index i


# Quick Sort Big O
# On average, quicksort has a Big O of O(n*log(n)). In the worst case, and assuming we don't take any steps to protect ourselves, it can degrade to O(n^2). partition() has a single for-loop that ranges from the lowest index to the highest index in the array. By itself, the partition() function is O(n). The overall complexity of quicksort is dependent on how many times partition() is called.

# Worst case: The input is already sorted. An already sorted array results in the pivot being the largest or smallest element in the partition each time, meaning partition() is called a total of n times.

# Best case: The pivot is the middle element of each sublist which results in log(n) calls to partition().


# Fixing Quick Sort
# While the version of quicksort that we implemented is almost always able to perform at speeds of O(n*log(n)), its Big O is still technically O(n^2) due to the worst-case scenario. We can fix this by altering the algorithm slightly.

# Two of the approaches are:

# Shuffle input randomly before sorting. This can trivially be done in O(n) time.
# Actively find the median of a sample of data from the partition, this can be done in O(1) time.
# Random Approach
# The random approach is easier to code, which is nice if you're the one writing the code.

# The function simply shuffles the list into random order before sorting it, which is an O(n) operation. The likelihood of shuffling a large list into sorted order is so low that it's not worth considering.

# Median Approach
# Another popular solution is to use the "median of three" approach. Three elements (for example: the first, middle, and last elements) of each partition are chosen and the median is found between them. That item is then used as the pivot.

# This approach has less overhead, and also doesn't require randomness to be injected into the function, meaning it can remain deterministic and pure.



def quick_sort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)
        quick_sort(nums, low, pi - 1)    
        quick_sort(nums, pi + 1, high)
    return nums
    


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    print(i)         
    return i        
      

print(quick_sort([9, 6, 2, 1, 8, 7], 0, 5)) # [-10, 1, 2,