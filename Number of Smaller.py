n, m = map(int, input().split())

n_array = list(map(int, input().split()))
m_array = list(map(int, input().split()))
i = 0
j = 0
result = []
while i < m:
    for k in range(j, n):
        if n_array[k] < m_array[i]:
            j += 1
        else:
            break
    result.append(j)
    i += 1
print(*result)
