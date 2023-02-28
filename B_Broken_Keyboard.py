tests = int(input())
for _ in range(tests):
    string = input()
    size = len(string)
    left = 0
    answer = set()
    while left < size:
        right = left + 1
        count = 1
        while right < size and string[right] == string[right - 1]:
            count += 1
            right += 1
            left += 1
        if count % 2 == 1 and string[left] not in answer:
            answer.add(string[left])
        left += 1
    answer = list(answer)
    print("".join(sorted(answer)))
