# Valid Anagram

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 

 **Example 1:** 

 **Input:**  s = "anagram", t = "nagaram"

 **Output:**  true

 **Example 2:** 

 **Input:**  s = "rat", t = "car"

 **Output:**  false

 

 **Constraints:** 

- 1 <= s.length, t.length <= 5 * 104
- s and t consist of lowercase English letters.

 

 **Follow up:**  What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 95.49%)  
**Memory:** 19.6 MB (beats 26.00%)  
**Submitted:** 2026-07-23T05:38:44.088Z  

```py
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if Counter(s) == Counter(t) else False
```

---

[View on LeetCode](https://leetcode.com/problems/valid-anagram/)