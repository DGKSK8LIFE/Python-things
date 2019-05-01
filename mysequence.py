def fib():
    x = 0
    while x > -1:
        x += 1
        y = (x - 1) + (x)
        if y >= 500:
            break
        else:
            print(y)

fib()
