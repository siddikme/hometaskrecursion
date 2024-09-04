def rec (x):
    if x<=5:
        print(x)
        rec(x+1)
        print(x)
rec(1)