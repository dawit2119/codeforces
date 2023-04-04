n = int(input())
array = list(map(int, input().split()))

for i in range(n-1):
    if (array[i] + array[i+1]) % 2 == 1:
        break
else:
    print(*array)
    exit()
array.sort()
print(*array)
