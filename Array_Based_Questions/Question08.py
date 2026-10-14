# Questions :--- 344. Reverse String

"""
Problem Statments :--

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]


Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""

# Code :--


def reverseString(str):
    left = 0
    right = len(str) - 1

    while left < right:
        str[left], str[right] = str[right], str[left]
        left += 1
        right -= 1


str = ["h", "e", "l", "l", "o"]
reverseString(str)
print(str)
