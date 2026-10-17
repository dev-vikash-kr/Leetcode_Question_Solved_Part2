# Questions :---- 1456. Maximum Number of Vowels in a Substring of Given Length

"""

Problem Statements :---

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3

Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2

Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

"""

# Code :---


def maxVowels(str, k):
    vowel = {"a", "e", "i", "o", "u"}

    left = 0
    current = 0
    result = 0

    for right in range(len(str)):
        current += 1 if str[right] in vowel else 0

        if right - left + 1 > k:
            current -= 1 if str[left] in vowel else 0
            left += 1

        result = max(result, current)
    return result


s = "aeiou"
k = 2

print(maxVowels(s, k))
