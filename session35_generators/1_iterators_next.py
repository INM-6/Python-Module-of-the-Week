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


LI = List_Iterator(colors)
# print(next(LI))
# print(next(LI))
# print(next(LI))
# print(next(LI))
# print(next(LI))
# print(next(LI))

# while(True):
#     try:
#         print(next(LI)[::-1])
#     except StopIteration:
#         break
