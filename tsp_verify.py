# Inputs:

# paths: A matrix where each point represents the distance between the two cities. For example, paths[cityA][cityB] holds the distance from cityA to cityB. paths[cityA][cityB] = paths[cityB][cityA]
# dist: The distance we are trying to find a path shorter than
# actual_path: The path we are trying to verify
# Algorithm:

# Loop over each city in the actual path
# Sum the distance between each city in the actual path
# If the sum is less than dist, return True, otherwise return False





def verify_tsp(paths, dist, actual_path):
    paths_sum = 0
    for i in range(1,len(actual_path)):
        print(i)
        paths_sum += paths[actual_path[i-1]][actual_path[i]]
    if paths_sum < dist:
        return True
    return False   


print(verify_tsp( [
            [0, 988, 523, 497],
            [988, 0, 414, 940],
            [523, 414, 0, 802],
            [497, 940, 802, 0],
        ],
        1060,
        [1, 0, 2, 3],)    )    