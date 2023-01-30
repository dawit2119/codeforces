def solve(grid):
    directions = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    n = 8

    for row in range(1, n - 1):
        for col in range(1, n - 1):
            if grid[row][col] != "#":
                continue
            bishop = True
            for di, dj in directions:
                row_n, col_n = row + di, col + dj
                bishop &= grid[row_n][col_n] == "#"
            if bishop:
                return (row + 1, col + 1)


test_cases = int(input())

for _ in range(test_cases):
    input()
    grid = [input() for _ in range(8)]
    print(*solve(grid))
