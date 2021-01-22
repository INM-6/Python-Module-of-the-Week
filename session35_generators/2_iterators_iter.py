colors = ['mauve', 'taupe', 'teal', 'razzmatazz', 'gamboge']


class List_Iterator():
    def __init__(self, ListyMcListface):
        self.ListyMcListface = ListyMcListface
        self.n = len(ListyMcListface)
        self.current_element = 0

    def __next__(self):
        if self.current_element == self.n:
            raise StopIteration
        else:
            return_value = self.ListyMcListface[self.current_element]
            self.current_element += 1
            return return_value


LI = iter(colors)
print(next(LI))
print(next(LI))
print(next(LI))
print(next(LI))

for c in iter(colors):
    print(c)

# or equivalently:
for c in colors:
    print(c)
