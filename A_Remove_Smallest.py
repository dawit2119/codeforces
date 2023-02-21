test_cases = int(input())

# for i in range(test_cases):
#     length = int(input())
#     array = list(map(int, input().split()))
#     array.sort()
#     size = 0  # to track if items having -1 or 0 difference
#     for i in range(length-1):
#         temp = array[i] - array[i+1]
#         if temp == -1 or temp == 0:
#             size += 1
#     if size == length - 1:
#         print("YES")
#     else:
#         print("NO")

for i in range(test_cases):
    length = int(input())
    array = list(map(int, input().split()))
    array.sort(reverse=True)
    size = 0
    for i in range(length-1):
        if size == length - 1:
            break
        if array[i] - array[i+1] <= 1:
            size += 1
    if size == length - 1:
        print("YES")
    else:
        print("NO")
