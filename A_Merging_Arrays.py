n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

left = right = 0
output = []
while left < n and right < m:
    if a[left] <= b[right]:
        output.append(a[left])
        left += 1
    else:
        output.append(b[right])
        right += 1

while left < n:
    output.append(a[left])
    left += 1
while right < m:
    output.append(b[right])
    right += 1
print(*output)
