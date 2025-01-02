# Bubble sort is a very basic sorting algorithm named for the way elements "bubble up" to the top of the list.

# Bubble sort repeatedly steps through a slice and compares adjacent elements, swapping them if they are out of order. It continues to loop over the slice until the whole list is completely sorted. Here's the pseudocode:

# Set swapping to True
# Set end to the length of the input list
# While swapping is True:
# Set swapping to False
# For i from the 2nd element to end:
# If the (i-1)th element of the input list is greater than the ith element:
# Swap the (i-1)th element and the ith element
# Set swapping to True
# Decrement end by one
# Return the sorted list


# Sometimes it's useful to know how the algorithm will perform based on what the input data is instead of just how much data there is. In the case of bubble sort (and many other algorithms), the best and worst case scenarios can actually change the time complexity.

# Best case: If the data is pre-sorted, bubble sort becomes really fast. Can you see why?
# Worst case: If the data is in reverse order, bubble sort becomes really slow (but still in the same complexity class as random data). Can you see why?


# Why Bubble Sort?
# Bubble sort is famous for how easy it is to write and understand.

# However, it's one of the slowest sorting algorithms, and as a result is almost never used in practice. That said, we covered it because it's a useful thought exercise so that you can appreciate why the more complex and performant algorithms are better. Let's cover those next.



def bubble_sort(nums):
    swapping = True
    end = len(nums)
    
    while swapping:
        swapping = False
        # print(end)
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                print(nums)
                swapping = True
        end -= 1
    
    return nums

