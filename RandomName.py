from functools import reduce
import random

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

# Picks a random fantasy name combination
def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)

# MAP to capitalize suffixes
def capitalize_suffix(name):
    return name.capitalize()

# FILTER return name with 'Fire'
def fire_in_name(name):
    return 'Fire' in name

# REDUCE name with 'Fire'
def concatenate_names(acc, name):
    return acc + ', ' + name

# DISPLAY all information
def display_name_info():
    for name in random_names:
        print(name)
    print(random_names_fire)
    print(concatenate_names_list)  

# Used MAP to capitalize suffixes
capitalized_suffixes = list(map(capitalize_suffix, suffixes))
# Used LIST COMPREHENSION to create a random name list
random_names = [create_fantasy_name(prefixes, capitalized_suffixes) for name in range(10)]
# Used FILTER to return only names with 'Fire'
random_names_fire = list(filter(fire_in_name, random_names))
# Used REDUCE to reduce brackets and quotes
concatenate_names_list = reduce(concatenate_names, random_names_fire)

# Used DISPLAY to show all information
display_name_info()