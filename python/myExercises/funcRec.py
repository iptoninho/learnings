def rec(x):
    i = 0
    while i <= 10:
        i = i + 1
        print (x-1) + i
        x = (x-1) + i
rec(10)
