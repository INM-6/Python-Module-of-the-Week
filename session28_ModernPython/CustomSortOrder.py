colors = ['mauve', 'taupe', 'teal', 'razzmatazz', 'gamboge']

# old way: Comparison Functions


def compare_length(c1, c2):
    if len(c1) < len(c2):
        return -1
    if len(c1) > len(c2):
        return 1
    return 0

# doesn't work anymore in Python3
# print(sorted(colors, cmp=compare_length))


# new way: Key functions
print(sorted(colors, key=len))
