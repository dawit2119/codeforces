n = int(input())
sequence = list(map(int, input().split()))
if n == 1:
    print(1, 0)
    exit()
e_sum, a_sum = sequence[0], sequence[-1]
left, right = 1, n-2
e_count, a_count = 1, 1,
while left <= right:
    if e_sum <= a_sum:
        e_sum += sequence[left]
        e_count += 1
        left += 1
    else:
        a_sum += sequence[right]
        a_count += 1
        right -= 1
print(e_count, a_count)
