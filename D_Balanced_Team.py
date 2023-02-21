n = int(input())
a = sorted(list(map(int, input().split())))

i = 0
j = 0
ans = 0

while i < n:
    while j < n and a[j] - a[i] <= 5:
        j += 1
    ans = max(ans, j - i)
    i += 1

print(ans)
