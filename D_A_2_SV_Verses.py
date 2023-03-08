n, a, b = map(int, input().split())

students = list(map(int, input().split()))
right = 0
sum = 0
count = 0
while right < n:
    sum += students[right]
    if sum <= b and sum >= a:
        count += 1
        sum = 0
    right += 1
print(count)
