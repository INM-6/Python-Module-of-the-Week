from collections import namedtuple
from itertools import zip_longest


def analyse_string(string):
    qs = string.count('q')
    ingredients = sorted(list(set(string)))
    d_p = sum((ord(s_c) - ord(s_p))**2 for s_c, s_p in zip_longest(
        string,
        'pineapple',
        fillvalue=chr(0)))
    return (qs, ingredients, d_p)


def sensible_analyse_string(string):
    Analysis = namedtuple('Analysis', [
        'number_of_qs',
        'sorted_letters',
        'pineapple_distance'
    ])
    qs = string.count('q')
    ingredients = sorted(list(set(string)))
    d_p = sum((ord(s_c) - ord(s_p))**2 for s_c, s_p in zip_longest(
        string,
        'pineapple',
        fillvalue=chr(0)))
    return Analysis(qs, ingredients, d_p)


print(analyse_string(string='kumquat'))
b = sensible_analyse_string('pineapple').number_of_qs
print(b)
