# def find_max(nums):

#     sorted_nums = sorted(nums)
#     return sorted_nums[-1]
    
    


def find_max(nums):
    max = -float("inf")
    
    for num in nums:
        print(num)
        print(max)
        if num > max:
            max = num
    return max
print(find_max([1, 2, 3, 4, 5]))