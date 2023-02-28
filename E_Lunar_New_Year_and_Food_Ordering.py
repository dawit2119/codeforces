n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

remaining = a[:]
total_cost = 0

for i in range(m):
    t, d = map(int, input().split())
    t -= 1  # 0-based indexing

    cost = 0
    if remaining[t] >= d:
        cost = d * c[t]
        remaining[t] -= d
    else:
        cost = remaining[t] * c[t]
        d -= remaining[t]
        remaining[t] = 0
        min_cost = min([c[j]
                       for j in range(n) if remaining[j] > 0] + [float('inf')])
        while d > 0 and min_cost != float('inf'):
            cheapest = [j for j in range(
                n) if remaining[j] > 0 and c[j] == min_cost][0]
            servings = min(d, remaining[cheapest])
            cost += servings * c[cheapest]
            remaining[cheapest] -= servings
            d -= servings
            min_cost = min([c[j] for j in range(
                n) if remaining[j] > 0] + [float('inf')])
    total_cost += cost
    print(cost)
