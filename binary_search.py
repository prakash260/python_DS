def binary_search(target, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return True
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

    

print(binary_search(10, [i for i in range(200)]))
print(binary_search(-1, [i for i in range(20000)]))