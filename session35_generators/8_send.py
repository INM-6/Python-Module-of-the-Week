def double_input_and_sum(n):
    s = 2*n
    while(True):
        n = yield s
        s += 2 * n


dias = double_input_and_sum(3)
next(dias)
for i in range(5):
    print(dias.send(i))

