test_cases = int(input())

for i in range(test_cases):
    no_of_planets, cost_of_second_machine = list(map(int, input().split()))
    orbits = list(map(int, input().split()))[:no_of_planets]
    unique_planets = set(orbits)
    unique_planets_length = len(unique_planets)
    print(min(unique_planets_length * cost_of_second_machine, no_of_planets * 1))
