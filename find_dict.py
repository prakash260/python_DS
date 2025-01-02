def find_last_name(names_dict, first_name):
    if first_name in names_dict:
        return names_dict[first_name]
    else:
        return None

    
# print(find_last_name({"John": "Doe", "Jane": "Smith"}, "John"))

print(find_last_name({"Key": "Error"}, None))