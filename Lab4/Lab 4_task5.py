from math import sqrt


def check(n):
    y = range(1, n + 1)
    squareY = [i**2 for i in y]
    l = []
    for i in y:
        for j in y:
            sum = i ** 2 + j ** 2
            if sum in squareY:
                l.append((i, j, sqrt(sum)))
    return l

# N is the range
combo = check(13)
print(combo)