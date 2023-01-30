test_cases = int(input())
for i in range(test_cases):
    test_case = list(map(int, input().split()))
    test_case = sorted(test_case, reverse=True)
    variation = test_case[-2] - test_case[-1]
    result = True
    for i in range(len(test_case)-2, -1, -1):
        variation += test_case[i-1] - test_case[i]
    print(variation)
