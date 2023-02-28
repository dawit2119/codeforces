t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    soldiers = list(map(int, input().strip()))
    for i in range(m):
        new_soldiers = soldiers.copy()
        for j in range(n):
            if soldiers[j] == 0:
                live_neighbors = 0
                if j > 0 and soldiers[j-1] == 1:
                    live_neighbors += 1
                if j < n-1 and soldiers[j+1] == 1:
                    live_neighbors += 1
                if live_neighbors == 1:
                    new_soldiers[j] = 1
            else:
                new_soldiers[j] = 1
        if soldiers == new_soldiers:
            break
        soldiers = new_soldiers
    print("".join(str(sol) for sol in soldiers))
