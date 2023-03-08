n, k = list(map(int, input().split()))

numbers = list(map(int, input().split()))
numbers.sort()
if k == 0:
    print(-1 if numbers[0] == 1 else 1)
    exit()

numbers.append(float('inf'))
index = k - 1
num = numbers[index]
if numbers[index+1] == num:
    print(-1)
    exit()
else:
    print(num)
    exit
