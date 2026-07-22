def sum_num(n, number):
    while True:
        swapped = False
        for i in range(n-1):
            if number[i] + number[i+1] <= 2 and number[i] > number[i+1]:
                number[i], number[i+1] = number[i+1], number[i]
                swapped = True
            
        if not swapped:
            break 
    return " ".join(map(str, number))
        
        

t_case = int(input())
for _ in range(t_case):
    n = int(input())
    number = list(map(int, input().split()))
    print(sum_num(n, number))
