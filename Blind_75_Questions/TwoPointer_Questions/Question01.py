# Questions :---  125. Valid Palindrome
# Types :-- Easy Mode

"""
Problem Statements :----

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


"""

# Code :----


def isPalidrome(str):
    left = 0
    right = len(str) - 1

    while left < right:
        if not str[left].isalnum():
            left += 1
            continue

        if not str[right].isalnum():
            right -= 1
            continue

        if str[left].lower() != str[right].lower():
            return False

        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"
print(isPalidrome(s))
