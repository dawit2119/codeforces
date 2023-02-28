def inpNum():
    return int(input())


def inpSepNum():
    return map(int, input().split())


def inpNumList():
    return list(map(int, input().split()))


test_cases = inpNum()
for _ in range(test_cases):
    n, k = inpSepNum()
    nums = inpNumList()
    subarrays = 0
    left = 0
    for right in range(1, n):
        # If the required condition failed move the left pointer to right
        if nums[right]*2 <= nums[right-1]:
            left = right
        # When the window size exceeds k increment subarrays
        if right - left >= k:
            subarrays += 1
    print(subarrays)
