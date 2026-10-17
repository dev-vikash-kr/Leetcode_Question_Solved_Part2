# Questions :---  438. Find All Anagrams in a String

"""
Problem Statements :---

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".


Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


"""

# Code :---
from collections import Counter


def findAnagrams(str, p):
    s_length = len(str)
    p_length = len(p)
    result = []

    if s_length < p_length:
        return result

    pattern_counter = Counter(p)
    window_counter = Counter(str[: p_length - 1])

    for i in range(p_length - 1, s_length):
        window_counter[str[i]] += 1

        if pattern_counter == window_counter:
            result.append(i - p_length + 1)

        left_char = str[i - p_length + 1]
        window_counter[left_char] -= 1

        if window_counter[left_char] == 0:
            del window_counter[left_char]

    return result


s = "cbaebabacd"
p = "abc"

print(findAnagrams(s, p))
