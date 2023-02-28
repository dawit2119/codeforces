from collections import defaultdict
n, k, q = map(int, input().split())
recipes = []
questions = []
for i in range(n):
    recipes.append(list(map(int, input().split())))
for i in range(q):
    questions.append(list(map(int, input().split())))
counter = [0] * 200001
for recipe in recipes:
    start, end = recipe
    counter[start] += 1
    if end + 1 < 200001:
        counter[end + 1] -= 1
for i in range(1, 200001):
    counter[i] += counter[i-1]
for i in range(200001):
    if counter[i] >= k:
        counter[i] = 1
    else:
        counter[i] = 0
for i in range(1, 200001):
    counter[i] += counter[i-1]

for query in questions:
    start, end = query
    if start - 1 >= 0:
        print(counter[end] - counter[start-1])
    else:
        print(counter[end] - counter[start-1])
