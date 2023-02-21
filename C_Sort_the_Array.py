input_size = int(input())
input_array = list(map(int, input().split()))
segments = []
swaps = 0
for i in range(input_size):
    for j in range(input_size-i-j):
        if input_array[j] > input_array[j+1]:
            swaps += 1
