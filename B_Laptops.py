number_of_laptops = int(input())
price_quality = [list(map(int, input().split()))
                 for _ in range(number_of_laptops)]

price_quality = sorted(price_quality)
for i in range(0, len(price_quality)-1):
    if price_quality[i][1] > price_quality[i+1][1]:
        print('Happy Alex')
        break
else:
    print("Poor Alex")
