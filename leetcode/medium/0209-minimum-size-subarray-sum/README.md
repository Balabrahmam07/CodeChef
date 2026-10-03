# Minimum Size Subarray Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of positive integers `nums` and a positive integer `target`, return  *the  **minimal length**  of a  **subarray**  whose sum is greater than or equal to*  `target`. If there is no such subarray, return `0` instead.

 

 **Example 1:** 

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

```

 **Example 2:** 

```
Input: target = 4, nums = [1,4,4]
Output: 1

```

 **Example 3:** 

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

```

 

 **Constraints:** 

- 1 <= target <= 109
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 104

 

 **Follow up:**  If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

## Solution

**Language:** Python  
**Runtime:** 19 ms (beats 47.00%)  
**Memory:** 30.6 MB (beats 43.10%)  
**Submitted:** 2026-10-03T02:43:26.126Z  

```py
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len_window = float('inf')
        sum_elements = 0
        left = 0
        for right in range(len(nums)):

            sum_elements += nums[right]

            while sum_elements >= target:
                min_len_window = min(min_len_window, right - left + 1)
                sum_elements -= nums[left]
                left += 1
        return min_len_window if min_len_window != float('inf') else 0
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)