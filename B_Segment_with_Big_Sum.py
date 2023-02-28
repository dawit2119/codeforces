n, s = list(map(int, input().split()))
array = list(map(int, input().split()))
total = left = 0
min_len = n + 1
for right in range(n):
    total += array[right]
    while left < n and total >= s:
        min_len = min(min_len, right - left + 1)
        total -= array[left]
        left += 1
print("0" if min_len == n + 1 else min_len)
