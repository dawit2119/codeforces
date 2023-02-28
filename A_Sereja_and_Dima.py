
n = int(input())
cards = list(map(int, input().split()))

left = 0
right = n - 1
sereja_sum = 0
dima_sum = 0
count = 0
while left <= right:
    if count % 2 == 0:
        if cards[left] >= cards[right]:
            sereja_sum += cards[left]
            left += 1
        else:
            sereja_sum += cards[right]
            right -= 1
    else:
        if cards[left] >= cards[right]:
            dima_sum += cards[left]
            left += 1
        else:
            dima_sum += cards[right]
            right -= 1
    count += 1
print(sereja_sum, dima_sum)
