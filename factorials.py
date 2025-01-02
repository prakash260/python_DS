def countdown(n):
    product = 1
    for i in range(1, n+1):
        product *= i
        
    return product
# print(countdown(5))

def decayed_followers(intl_followers, fraction_lost_daily, days):
    
    for i in range(days):
        intl_followers = intl_followers - intl_followers * fraction_lost_daily

    return intl_followers

print(decayed_followers(1000, 0.05, 3))