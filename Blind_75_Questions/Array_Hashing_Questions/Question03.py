# Questions :- 242. Valid Anagram
#  Types :-- Easy

"""

Problem Statements :----

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false


"""

# Code :----


# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False

#     chars = {}

#     for ch in s:
#         chars[ch] = chars.get(ch, 0) + 1

#     for ch in t:
#         if ch not in chars:
#             return False

#         else:
#             if chars[ch] == 0:
#                 return False

#             chars[ch] -= 1

#     return True


# s = "anagram"
# t = "nagaram"
# print(isAnagram(s, t))


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    chars = {}

    for ch in s:
        chars[ch] = chars.get(ch, 0) + 1

    for ch in t:
        if ch not in chars:
            return False

        else:
            if chars[ch] == 0:
                return False

        chars[ch] -= 1

    return True


s = "anagram"

t = "hfhsh"
print(isAnagram(s, t))
