from collections import defaultdict
n, m = map(int, input().split())
wood = []
for i in range(n):
    wood.append(input().strip())
rows_count = [[0] * 26 for _ in range(n)]
cols_count = [[0] * 26 for _ in range(m)]

for row in range(n):
    for item in wood[row]:
        rows_count[row][ord(item) - ord('a')] += 1
for col in range(m):
    for row in range(n):
        cols_count[col][ord(wood[row][col]) - ord('a')] += 1
output = ""
for row in range(n):
    for col in range(m):
        char = wood[row][col]
        item = ord(char) - ord('a')
        temp = rows_count[row][item] + cols_count[col][item]
        if temp == 2:
            output += char
print(output)
