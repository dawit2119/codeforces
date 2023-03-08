t = int(input())

for i in range(t):
    n = int(input())
    wights = list(map(int,input().split()))

    low = -1
    high = sum(wights)
    