t_case = int(input())
for _ in range(t_case):
    n, x = map(int, input().split())
    
    if n % 2 == 0:
        print("yes")
    else:
        if x % 2 == 0:
            print("no")
        else:
            print("yes")
