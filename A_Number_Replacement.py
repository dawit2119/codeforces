test_case = int(input())
for i in range(test_case):
    length = int(input())
    nums = list(map(int, input().split()))
    chars = input()
    num_char_map = {}
    for i, num in enumerate(nums):
        if num in num_char_map and num_char_map[num] != chars[i]:
            print('NO')
            break
        else:
            num_char_map[num] = chars[i]
    else:
        print("YES")
