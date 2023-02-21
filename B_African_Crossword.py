from collections import defaultdict
n, m = list(map(int, input().split()))
crossword = []
for i in range(n):
    crossword.append(input())
rows = defaultdict(int)
cols = defaultdict(int)
for i in range(m):
    temp = ""
    for j in range(m):
        temp += crossword[i][j]
    rows.append(temp)

for j 

