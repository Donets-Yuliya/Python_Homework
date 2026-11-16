def reduce(*args, action):
    
    def func(i):
        if i == 1:
            return action(args[i-1], args[i])
        return action(func(i-1), args[i])

    return func(len(args)-1)

summa = reduce(1, 2, 3, action=lambda x, y: x + y)
print(summa) # 6

minimum = reduce(
    1,
    2,
    3,
    0,
    action=lambda x, y: x if x < y else y
)
print(minimum) # 0

product = reduce(
    2,
    3,
    4,
    action=lambda x, y: x * y
)
print(product) # 24
