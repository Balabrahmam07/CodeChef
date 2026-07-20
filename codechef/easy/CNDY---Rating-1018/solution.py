def Check_price(cities, candies):
    if len(candies) % cities != 0:
        return "NO"
    
    for i in candies:
        if candies.count(i) > 2:
            return "NO"
    return "YES"





t_case = int(input())
for _ in range(t_case):
    cities = int(input())
    candies = list(map(int, input().split()))
    print(Check_price(cities, candies))