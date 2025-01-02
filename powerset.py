# - Check if the input list is empty. If it is, return a list containing an empty list. (The power set of an empty set is a set containing only the empty set)
# - Otherwise, create an empty list to hold all the final subsets of the input list.
# - Recursively call power_set. Pass in all of the elements in the input set except the first one.
# - Iterate over the list of subsets returned from the recursive call. For each subset, append two new subsets to the final list of subsets:
#       1. list_with_only_the_first_item_from_input_set + subset
#     2. subset
# - Return the list of subsets

def power_set(input_set):
    if not input_set:
        return [[]]
    else:
        power_set_without_first = power_set(input_set[1:])
        with_first = [[input_set[0]] + rest for rest in power_set_without_first]
        # print(with_first)
        return with_first + power_set_without_first
    
    

# print(power_set([1, 2, 3])) # [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

# def halved_sections(n):
#     rows = []
#     i = n
#     while i > 0:
#         col = []
#         for j in range(i+1):
#             col.append(j)
#         rows.append(col)
#         i //= 2
#     return rows

# print(halved_sections(12))

# def power_set(input_set):
#     if len(input_set) == 0:
#         return [[]]

#     subsets = []
#     first = input_set[0]
#     remaining = input_set[1:]
#     remaining_subsets = power_set(remaining)
#     for subset in remaining_subsets:
#         subsets.append([first] + subset)
#         subsets.append(subset)
#     return subsets
