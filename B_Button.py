test_cases = int(input())

for i in range(test_cases):
    test_case = input()
    temp = [0] * 26
    last_index = [0] * 26
    for char in test_case:
        temp[ord(char)-ord('a')] += 1
    output = ''
    for index, item in enumerate(temp):
        if item % 2 == 1:
            output += (chr(index + ord('a')))
    print(output)
