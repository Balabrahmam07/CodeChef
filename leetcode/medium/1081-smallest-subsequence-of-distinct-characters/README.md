# Smallest Subsequence of Distinct Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, return  *the  **lexicographically smallest*   *subsequence**  of*  `s`  *that contains all the distinct characters of*  `s`  *exactly once*.

 

 **Example 1:** 

```
Input: s = "bcabc"
Output: "abc"

```

 **Example 2:** 

```
Input: s = "cbacdcbc"
Output: "acdb"

```

 

 **Constraints:** 

- 1 <= s.length <= 1000
- s consists of lowercase English letters.

 

 **Note:**  This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 75.23%)  
**Submitted:** 2026-07-19T14:51:23.155Z  

```py
class Solution:
    def smallestSubsequence(self, s: str) -> str:

        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        stack = []
        visited = set()
        

        for idx, char in enumerate(s):

            if char in visited:
                continue
                
         
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > idx:
         
                removed_char = stack.pop()
                visited.remove(removed_char)
                
        
            stack.append(char)
            visited.add(char)
            
    
        return "".join(stack)
```

---

[View on LeetCode](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)