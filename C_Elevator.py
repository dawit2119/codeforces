t = int(input())

for i in range(t):
    wt, et, ef = map(int, input().split())
    path_one = wt * 4
    path_two = wt * ef + (4-ef) * et
    path_three = ef * et + et * 4
    print(min(path_one, path_two, path_three))
