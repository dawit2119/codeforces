from collections import defaultdict
test_cases = int(input())
for i in range(test_cases):
    row, column = list(map(int, input().split()))
    board = []
    for i in range(row):
        items = list(map(int, input().split()))
        board.append(items)
    right_diagonal = defaultdict(int)
    left_diagonal = defaultdict(int)

    for i in range(row):
        for j in range(column):
            right_diagonal[i+j] += board[i][j]
            left_diagonal[i-j] += board[i][j]
    max_score = 0
    for i in range(row):
        for j in range(column):
            max_score = max(
                max_score, (left_diagonal[i-j] + right_diagonal[i+j] - board[i][j]))
    print(max_score)
