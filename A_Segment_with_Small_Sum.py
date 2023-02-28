n, s = list(map(int, input().split()))
array = list(map(int, input().split()))

left = 0
current_sum = 0
length = 0
for right in range(n):
    current_sum += array[right]
    if current_sum <= s:
        length = max(right-left+1, length)
    else:
        current_sum -= array[left]
        left += 1
print(length)
