# ADDDICE

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Adding Dice

You have $2$ dice with you, and you really like the number $9$. You want the sum of both numbers on the die to add to $9$.

You rolled the first dice, and it showed a number $X$.

Given the roll of the first dice, is it still possible for both die to add to $9$? Print $\text{Yes}$ if it is possible or $\text{No}$ otherwise.

### Input Format
- The first and only line of each test case contains a single integer $X$.
### Output Format

Output $\text{Yes}$ if it is possible for both die to add to $9$ and $\text{No}$ otherwise.

### Constraints
- $1 \le X \le 6$
### Sample 1:
Input
Output

```
3

```

```
Yes

```

### Explanation:

The second dice could show a $6$, and then both would add to a $9$.

### Sample 2:
Input
Output

```
1

```

```
No

```

### Explanation:

There are no possible rolls of the second die that add to $9$ after rolling a $1$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-22T17:20:49.398Z  

```py
diec = int(input())

if 2 < diec < 9:
    print("YES")
else:
    print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/ADDDICE)