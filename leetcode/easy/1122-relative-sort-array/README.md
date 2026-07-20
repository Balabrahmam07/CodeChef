# Relative Sort Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two arrays `arr1` and `arr2`, the elements of `arr2` are distinct, and all elements in `arr2` are also in `arr1`.

Sort the elements of `arr1` such that the relative ordering of items in `arr1` are the same as in `arr2`. Elements that do not appear in `arr2` should be placed at the end of `arr1` in  **ascending**  order.

 

 **Example 1:** 

```
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

```

 **Example 2:** 

```
Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]

```

 

 **Constraints:** 

- 1 <= arr1.length, arr2.length <= 1000
- 0 <= arr1[i], arr2[i] <= 1000
- All the elements of arr2 are distinct.
- Each arr2[i] is in arr1.

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.5 MB  
**Submitted:** 2026-07-20T16:46:42.220Z  

```py
from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        final_arr = []
        counts = Counter(arr1)
        for i in arr2:
            final_arr.extend([i] * counts[i])
            for _ in range(counts[i]):
                arr1.remove(i)
        return final_arr + sorted(arr1)
        
```

---

[View on LeetCode](https://leetcode.com/problems/relative-sort-array/)