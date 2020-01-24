from functools import partial
# ugly:
with open('./IterSentinel.py', 'r') as f:
    blocks = []
    while True:
        block = f.read(3)
        if block == '###':
            break
        blocks.append(block)
print(blocks)

######


# nice:
with open('./IterSentinel.py', 'r') as f:
    blocks = []
    for block in iter(partial(f.read, 3), '###'):
        blocks.append(block)
print(blocks)
