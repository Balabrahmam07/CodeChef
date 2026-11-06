# Count Vowels Permutation

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an integer `n`, your task is to count how many strings of length `n` can be formed under the following rules:

- Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
- Each vowel 'a' may only be followed by an 'e'.
- Each vowel 'e' may only be followed by an 'a' or an 'i'.
- Each vowel 'i' may not be followed by another 'i'.
- Each vowel 'o' may only be followed by an 'i' or a 'u'.
- Each vowel 'u' may only be followed by an 'a'.

Since the answer may be too large, return it modulo `10^9 + 7`.

 

 **Example 1:** 

```
Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i", "o" and "u".

```

 **Example 2:** 

```
Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

```

 **Example 3:** 

```
Input: n = 5
Output: 68
```

 

 **Constraints:** 

- 1 <= n <= 2 * 10^4

## Solution

**Language:** Python  
**Runtime:** 85 ms (beats 61.79%)  
**Memory:** 19.2 MB (beats 70.15%)  
**Submitted:** 2026-11-06T08:48:06.776Z  

```py
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7

        a = e = i = o = u = 1
         
        for _ in range(n-1):
            new_a = e + i + u
            new_e = a + i
            new_i = e + o
            new_o = i
            new_u = i + o

            a, e, i, o, u = (
                new_a % MOD,
                new_e % MOD,
                new_i % MOD,
                new_o % MOD,
                new_u % MOD
            )
        return (a + e + i + o + u) % MOD

        
```

---

[View on LeetCode](https://leetcode.com/problems/count-vowels-permutation/)