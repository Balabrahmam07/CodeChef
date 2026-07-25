# Search Insert Position

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

 

 **Example 1:** 

```
Input: nums = [1,3,5,6], target = 5
Output: 2

```

 **Example 2:** 

```
Input: nums = [1,3,5,6], target = 2
Output: 1

```

 **Example 3:** 

```
Input: nums = [1,3,5,6], target = 7
Output: 4

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums contains distinct values sorted in ascending order.
- -104 <= target <= 104

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.8 MB (beats 81.10%)  
**Submitted:** 2026-07-25T05:50:41.150Z  

```py
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right  = len(nums) - 1
        while left <= right:
            mid = (left + right)  // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                min_target = mid
            else:
                right = mid - 1

        return left
        
```

---

[View on LeetCode](https://leetcode.com/problems/search-insert-position/)