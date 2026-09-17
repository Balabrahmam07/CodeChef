# Find Two Non-overlapping Sub-arrays Each With Target Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array of integers `arr` and an integer `target`.

You have to find  **two non-overlapping sub-arrays**  of `arr` each with a sum equal `target`. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is  **minimum**.

Return  *the minimum sum of the lengths*  of the two required sub-arrays, or return `-1` if you cannot find such two sub-arrays.

 

 **Example 1:** 

```
Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.

```

 **Example 2:** 

```
Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.

```

 **Example 3:** 

```
Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.

```

 

 **Constraints:** 

- 1 <= arr.length <= 105
- 1 <= arr[i] <= 1000
- 1 <= target <= 108

## Solution

**Language:** Python  
**Runtime:** 133 ms (beats 61.45%)  
**Memory:** 31.2 MB (beats 66.48%)  
**Submitted:** 2026-09-17T06:20:04.696Z  

```py
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        left = 0


        current_sum = 0

        best = [float("inf")] * len(arr)

        answer = float("inf")

        for right in range(len(arr)):

            current_sum += arr[right]

            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:

                length = right - left + 1

                if left > 0:
                    answer = min(answer, length + best[left - 1])

                best[right] = min(best[right], length)

            if right > 0:
                best[right] = min(best[right], best[right - 1])
        return -1 if answer == float('inf') else answer
```

---

[View on LeetCode](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/)