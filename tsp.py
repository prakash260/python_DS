# Use the permutations function to get the matrix of all possible paths through the given cities. Where the first path, [0, 1, 2] represents moving from city 0 -> city 1 -> city 2
# Iterate over each possible path (permutation)
# Sum the distances between each city in the path using the paths matrix to look up the distances
# If the total distance of the path is less than the given dist return True
# If no short paths were found, return False

def tsp(cities, paths, dist):
    possible_paths = permutations(cities)
    for path in possible_paths:
        total_dist = 0
        for i in range(len(cities) - 1):
            total_dist += paths[path[i]][path[i + 1]]
        if total_dist < dist:
            return True
    return False


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

print(tsp( [0, 1, 2, 3, 4, 5, 6, 7],
        [
            [0, 63, 824, 940, 561, 937, 14, 95],
            [63, 0, 736, 860, 408, 727, 844, 803],
            [824, 736, 0, 684, 640, 1, 626, 505],
            [940, 860, 684, 0, 847, 888, 341, 249],
            [561, 408, 640, 847, 0, 747, 333, 720],
            [937, 727, 1, 888, 747, 0, 891, 64],
            [14, 844, 626, 341, 333, 891, 0, 195],
            [95, 803, 505, 249, 720, 64, 195, 0],
        ],
        1066))