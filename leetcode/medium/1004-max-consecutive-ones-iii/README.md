# Max Consecutive Ones III

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a binary array `nums` and an integer `k`, return  *the maximum number of consecutive* `1` *'s in the array if you can flip at most*  `k` `0`'s.

 

 **Example 1:** 

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

 **Example 2:** 

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.
- 0 <= k <= nums.length

## Solution

**Language:** Python  
**Runtime:** 51 ms (beats 85.77%)  
**Memory:** 22.1 MB (beats 86.33%)  
**Submitted:** 2026-10-03T03:22:07.776Z  

```py
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        max_count = 0
        zero_count = 0

        for right in range(len(nums)):
            
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_count = max(max_count, right - left + 1)
        return max_count

        
```

---

[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)