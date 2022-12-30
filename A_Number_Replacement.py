def can_be_replaced(nums, chars):

    num_char_map = {}  # takes num with their assigned character
    for i, num in enumerate(nums):
        if num in num_char_map and num_char_map[num] != chars[i]:
            # if the assigned character to the number not matched
            print('NO')
            break
        else:
            num_char_map[num] = chars[i]
    else:
        print("YES")


if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        length = int(input())
        nums = list(map(int, input().split()))
        chars = input()
        can_be_replaced(nums, chars)
