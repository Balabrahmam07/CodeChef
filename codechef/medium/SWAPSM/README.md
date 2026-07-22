# SWAPSM

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Swap Small

You have an array $A$ consisting of $N$ integers such that $0 \le A_i \le 2$.

You can do the following operation multiple times:

- Choose an index $i$ ($1 \le i < N$) such that $A_i + A_{i + 1} \le 2$
- Swap $A_i$ and $A_{i + 1}$.

Find the lexicographically smallest array $A$ possible with these swaps.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the lexicographically smallest array possible.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 100$
- $0 \le A_i \le 2$
### Sample 1:
Input
Output

```
2
4
1 0 2 1
5
2 2 2 0 0

```

```
0 1 2 1
0 0 2 2 2
```

### Explanation:

 **Test Case 1:**  Swap $A_1$ and $A_2$ to get $[0, 1, 2, 1]$. This is the minimal array possible, and there are no other operations possible. For example, we cannot swap $A_3$ and $A_4$ because they sum to $3$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-22T18:00:20.562Z  

```py
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

```

---

[View on CodeChef](https://www.codechef.com/problems/SWAPSM)