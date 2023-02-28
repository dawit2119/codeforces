n, s = list(map(int, input().split()))
array = list(map(int, input().split()))

left = 0
current_sum = 0
good_sum = 0
length = 0
for right in range(n):
    current_sum += array[right]
    if current_sum > s:
        current_sum -= array[left]
    left += 1
    if current_sum <= s:
        length = max(length, right-left + 1)
        good_sum = max(current_sum, good_sum)
print(good_sum)
