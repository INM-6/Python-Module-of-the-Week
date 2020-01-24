from collections import deque

colors = ['mauve', 'taupe', 'teal', 'razzmatazz', 'gamboge']


del colors[0]
colors.pop(0)
colors.insert(0, 'amaranth')

colors = deque(colors)

del colors[0]
colors.popleft()
colors.appendleft('amaranth')
