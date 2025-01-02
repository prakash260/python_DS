# Merge sort is a recursive sorting algorithm and it's quite a bit faster than bubble sort. It's a divide and conquer algorithm.:

# Divide: divide the large problem into smaller problems, and recursively solve the smaller problems
# Conquer: Combine the results of the smaller problems to solve the large problem
# In merge sort we:

# Divide the array into two (equal) halves (divide)
# Recursively sort the two halves
# Merge the two halves to form a sorted array (conquer)

# Algorithm
# The algorithm consists of two separate functions, merge_sort() and merge().

# merge_sort() divides the input array into two halves, calls itself on each half, and then merges the two sorted halves back together in order.

# The merge() function merges two already sorted lists back into a single sorted list. At the lowest level of recursion, the two "sorted" lists will each only have one element. Those single element lists will be merged into a sorted list of length two, and we can build from there.

# In other words, all the "real" sorting happens in the merge() function.

# merge_sort() pseudocode
# Input: A, an unsorted list of integers

# If the length of A is less than 2, it's already sorted so return it
# Split the input array into two halves down the middle
# Call merge_sort() twice, once on each half
# Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls
# merge() pseudocode
# Inputs: A and B. Two sorted lists of integers

# Create a new final list of integers.
# Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
# Use a loop to iterate over A and B at the same time. If an element in A is less than or equal to its respective element in B, add it to the final list and increment i. Otherwise, add the item in B to the final list and increment j.
# After comparing all the items, there may be some items left over in either A or B. Add those extra items to the final list.
# Return the final list.


# Why Merge Sort?
# Pros:

# Fast: Merge sort is much faster than bubble sort. O(n*log(n)) instead of O(n^2).
# Stable: Merge sort is a stable sort which means that values with duplicate keys in the original list will be in the same order in the sorted list.
# Cons:

# Memory usage: Most sorting algorithms can be performed using a single copy of the original array. Merge sort requires extra subarrays in memory.
# Recursive: Merge sort requires many recursive function calls, and in many languages (like Python), this can incur a performance penalty.

# def merge_sort(nums):
#     print(len(nums))
#     if len(nums) < 2:
#         return nums
#     half = len(nums) // 2
#     first = merge_sort(nums[:half])
#     second = merge_sort(nums[half:])
#     return merge(first, second)

# def merge(first, second):
#     final = []
#     i, j = 0, 0
#     while i < len(first) and j < len(second):
#         if first[i] <= second[j]:
#             final.append(first[i])
#             i += 1
#         else:
#             final.append(second[j])
#             j += 1
#     final.extend(first[i:])
#     final.extend(second[j:])
#     return final

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    sorted_left_side = merge_sort(nums[: len(nums) // 2])
    sorted_right_side = merge_sort(nums[len(nums) // 2 :])
    return merge(sorted_left_side, sorted_right_side)


def merge(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        print(i, j)
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final




print(merge_sort([67,98,1,33,41]))
