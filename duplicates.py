# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)


class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"


# dont touch above this line


def vanity(influencer):
    return  (influencer.num_bio_links * 5) + influencer.num_selfies 

    

def vanity_sort(influencers):
    return sorted(influencers, key=lambda influencer: vanity(influencer), reverse=False)


print(vanity_sort([badcop, lane]))