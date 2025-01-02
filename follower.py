def get_estimated_spread(audiences_followers):
    # num_followers = float('inf')
    if len(audiences_followers) == 0:
        return 0
    num_followers = len(audiences_followers)
    average_audience_followers = (sum(audiences_followers)/len(audiences_followers))
    estimated_spread = average_audience_followers * ( num_followers ** 1.2 )
    return estimated_spread

audiences_followers = [2, 3, 2, 19]
audiences_followers =[0,0]
print(get_estimated_spread(audiences_followers))