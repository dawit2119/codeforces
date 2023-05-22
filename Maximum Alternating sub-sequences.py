t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    maxmimum  = nums[0]
    res = []

    for i in range(1,n):
        if nums[i] * nums[i-1] > 0:
            maxmimum = max(maxmimum,nums[i])
        else:
            res.append(maxmimum)
            maxmimum = nums[i]
    res.append(maxmimum)
    print(sum(res))
