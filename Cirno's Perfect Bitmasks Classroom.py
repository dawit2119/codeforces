t = int(input())

for _ in range(t):
    x = int(input())
    if x == 1:
        print(3)
    else:
        temp = x ^ (x & (x-1))
        if temp ^ x:
            print(temp)
        else:
            print(temp + 1)
