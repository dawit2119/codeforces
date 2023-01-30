card_length = int(input())

cards = list(map(int, input().split()))

wube_sum = 0
henok_sum = 0
left = 0
right = card_length - 1
count = 0
while left <= right:
    if count % 2 == 0:
        if cards[left] > cards[right]:
            wube_sum += cards[left]
            left += 1
        else:
            wube_sum += cards[right]
            right -= 1
    else:
        if cards[left] > cards[right]:
            henok_sum += cards[left]
            left += 1
        else:
            henok_sum += cards[right]
            right -= 1
    count += 1

print(wube_sum, henok_sum)
