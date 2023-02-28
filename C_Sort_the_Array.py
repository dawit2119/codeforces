from math import inf


n = int(input())

array = list(map(int, input().split()))
sorted_array = sorted(array)

start, end = inf, -inf

for idx in range(n):
    if array[idx] != sorted_array[idx]:
        start = min(start, idx)
        end = idx

if start == inf:
    print("yes")
    print(1, 1)
else:
    i, j = start, end

    while i <= end:
        if array[i] != sorted_array[j]:
            print("no")
            exit()

        i += 1
        j -= 1

    print("yes")
    print(start + 1, end + 1)
