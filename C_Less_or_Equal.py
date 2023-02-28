n, k = list(map(int, input().split()))

numbers = list(map(int, input().split()))
numbers.sort()
nums_count = [0] * (numbers[-1] + 1)
for num in numbers:
    nums_count[num] += 1
for i in range(1, len(nums_count)):
    nums_count[i] += nums_count[i-1]
value = -1
for i in range(len(nums_count)):
    if nums_count[i] == k:
        value = i
        break

print(value)
