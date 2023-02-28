n = int(input())
array = list(map(int, input().split()))

for i in range(n-1):
    if array[i] % 2 == 1 and array[i+1] % 2 == 1:
        continue
    else:
        array[i], array[i+1] = array[i+1], array[i]

print(*array)
