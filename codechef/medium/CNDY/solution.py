from collections import Counter

def Check_price(cities, candies):
    
    frequency = Counter(candies)
    
    for count in frequency.values():
        if count > 2:
            return "NO"
    return "YES"

t_case = int(input())
for _ in range(t_case):
    cities = int(input())
    candies = list(map(int, input().split()))
    print(Check_price(cities, candies))