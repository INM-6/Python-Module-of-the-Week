colors = ['mauve', 'taupe', 'teal', 'razzmatazz', 'gamboge']


def operation(c):
    return c[::-1].capitalize()


color_iterator = (operation(color) for color in colors if color != 'teal')

for c in color_iterator:
    print(c)
