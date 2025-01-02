import math

print(f"Logarithm base 2 of 16 is: {math.log(9, 3)}")




def log_scale(data, base):
    return [math.log(x, base) for x in data]

print(log_scale([1, 10, 100, 1000], 10))


