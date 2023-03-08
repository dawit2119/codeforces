t = int(input())


def isPossible(mid, dividers, n):
    current = 0
    if mid == 0:
        return dividers[0]
    for i in range(mid):
        current += dividers[i]
        if current >= n:
            break
    return current >= n


for i in range(t):
    n, m = map(int, input().split())
    dividers = list(map(int, input().split()))
    dividers = sorted(dividers)
    low = -1
    high = max(dividers)
    total_sum = sum(dividers)
    if total_sum < n:
        print(-1)
        continue
    while high > low + 1:
        mid = low + (high - low) // 2
        if isPossible(mid, dividers, n):
            high = mid
        else:
            low = mid
    print(high)
