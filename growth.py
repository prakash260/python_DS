def exponential_growth(n, factor, days):
    growth = [n]
    if factor != 0 and days != 0:
        for i in range(days):
            val_append = (factor * growth[len(growth)-1])
            growth.append(val_append)
    return growth


print(exponential_growth(10, 2, 4))