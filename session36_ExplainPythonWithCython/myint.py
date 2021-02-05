# cython: language_level=3


class MyInt:
    def __init__(self, val):
        self.val = int(val)

    def __iadd__(self, other):
        self.val += other
        return self

    def __repr__(self):
        return str(self.val)


age_variable = MyInt(20)
age_variable += 4
print(age_variable)
