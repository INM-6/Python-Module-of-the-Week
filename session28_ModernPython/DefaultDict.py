from collections import defaultdict
from pprint import pprint

Pizza_Ingredients = [
    'tomatoes',
    'flour',
    'water',
    'mozzarella',
    'pineapple',
    'tomatoes',
    'paella',
]


# typical dict-stuff:
def oldschool_count():
    count = {}
    for ingredient in Pizza_Ingredients:
        if ingredient not in count.keys():
            count[ingredient] = 0
        count[ingredient] += 1
    pprint(count)


def oldschool_cluster():
    length = {}
    for ingredient in Pizza_Ingredients:
        l = len(ingredient)
        try:
            length[l].append(ingredient)
        except KeyError:
            length[l] = [ingredient]
    pprint(length)


# A bit nicer:
def count_via_get():
    count = {}
    for ingredient in Pizza_Ingredients:
        count[ingredient] = count.get(ingredient, 0) + 1
    pprint(count)


# now with neat defaultdicts:
def defaultdict_count():
    count = defaultdict(int)
    for ingredient in Pizza_Ingredients:
        count[ingredient] += 1
    pprint(dict(count))


def defaultdict_cluster():
    length = defaultdict(list)
    for ingredient in Pizza_Ingredients:
        length[len(ingredient)].append(ingredient)
    pprint(dict(length))

# defaultdict can take arbitrary generators:
def f():
    return 2


d = defaultdict(f)
d[1] = 2
d[2]
print(dict(d))

d2 = defaultdict(lambda: defaultdict(list))
d2[1][2].append(3)
print(dict(d2))
"""
"""