# Ransom Note

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `ransomNote` and `magazine`, return `true` *if* `ransomNote` *can be constructed by using the letters from* `magazine` *and* `false` *otherwise*.

Each letter in `magazine` can only be used once in `ransomNote`.

 

 **Example 1:** 

```
Input: ransomNote = "a", magazine = "b"
Output: false

```

 **Example 2:** 

```
Input: ransomNote = "aa", magazine = "ab"
Output: false

```

 **Example 3:** 

```
Input: ransomNote = "aa", magazine = "aab"
Output: true

```

 

 **Constraints:** 

- 1 <= ransomNote.length, magazine.length <= 105
- ransomNote and magazine consist of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 11 ms (beats 90.59%)  
**Memory:** 19.6 MB (beats 32.94%)  
**Submitted:** 2026-07-23T06:01:36.334Z  

```py
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = Counter(ransomNote)
        x = Counter(magazine)
        for i in s:
            if x[i] < s[i]:
                return False
        return True
```

---

[View on LeetCode](https://leetcode.com/problems/ransom-note/)