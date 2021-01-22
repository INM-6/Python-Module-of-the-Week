colors = ['mauve', 'taupe', 'teal', 'razzmatazz', 'gamboge']

AllTheColors = ''.join(colors)
print(AllTheColors)

SomeNumber = sum(len(c) for c in colors)
print(SomeNumber)

SomeOtherNumber = sum((len(c) for c in colors), start=17)
print(SomeOtherNumber)


