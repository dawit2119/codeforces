size = int(input())

names = input().split()

q = int(input())
for i in range(q):
    query = input()
    low = -1
    high = size
    while high > low + 1:
        mid = low + (high - low) // 2
        if query > names[mid]:
            low = mid
        else:
            high = mid
    print(high)
