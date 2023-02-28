from collections import deque
t = int(input())
for i in range(t):
    n = int(input())
    evilness = list((map(int, input().split())))
    i = 0
    while i < n and evilness[i] == 0:
        i += 1
    curr_sum = 0
    while i < n-1:
        if evilness[i] == 0:
            curr_sum += 1
        else:
            curr_sum += evilness[i]
        i += 1
    print(curr_sum)
