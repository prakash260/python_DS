def get_avg_brand_followers(all_handles, brand_name):
    allhandles = len(all_handles)
    count = 0
    for handles in all_handles:
        for handle in handles:
            if brand_name in handle:
                count += 1
    return count
    
    


all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
]
brand_name = "cosmo"

print(get_avg_brand_followers(all_handles, brand_name))