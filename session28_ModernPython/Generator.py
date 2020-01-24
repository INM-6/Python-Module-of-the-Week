from random import randint, choice
Pizza_Ingredients = [
    'tomatoes',
    'flour',
    'water',
    'yeast',
    'mozzarella',
    'pineapple',
    'paella',
    'mushrooms',
    'spinach (frozen)',
    'kiwi',
    'mashed potatoes',
    'banana'
]
stuff_i_do_not_like = [
    'water',
    'flour'
]


def safe_food(ingredients, leave_out):
    for ingredient in ingredients:
        if ingredient not in leave_out:
            yield ingredient


def adapted_recipe(ingredients, leave_out):
    units = ['stone', 'yard', 'torr^2/horsepower', 'morgen', 'handful', 'metric decipound']
    for ingredient in safe_food(ingredients, leave_out):
        yield f"{randint(1, 5)} {choice(units)} {ingredient}"

"""

for item in adapted_recipe(
    ingredients=Pizza_Ingredients,
    leave_out=stuff_i_do_not_like,
):
    print(item)


"""
def adapted_recipe_hungry(ingredients, leave_out):
    units = ['stone', 'yard', 'torr^2/horsepower', 'morgen', 'handful', 'metric decipound']
    hunger = 0
    for ingredient in safe_food(ingredients, leave_out):
        hunger = yield f"{randint(1, 5) + hunger} {choice(units)} {ingredient}"


recipe_generator = adapted_recipe_hungry(
    Pizza_Ingredients,
    stuff_i_do_not_like)
recipe_generator.send(None)
for hunger in range(len(Pizza_Ingredients)):
    try:
        print(recipe_generator.send(hunger))
    except(StopIteration):
        break
