n = int(input())
arr = list(map(int,input().split()))
max_size = 1
curr_size = 1
for i in range(1, len(arr)):
    if arr[i] >= arr[i-1]:
        curr_size += 1
    else:
        max_size = max(max_size, curr_size)
        curr_size = 1     
max_size = max(max_size, curr_size)
print(max_size)
        