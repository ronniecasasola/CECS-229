def fibo(n):
    num = []
    for i in range(n + 1):
        if i == 0:
            num.append(1)
        elif i == 1:
            num.append(1)
        else:
            num.append(num[i - 1] + num[i - 2])

    return num

start = 3
end = 25

fiboNumbers = fibo(end)

y = list(range(start, end + 1))

for i in fiboNumbers:
    if i in y:
        print(i)