# Questions :--- 20. Valid Parentheses.
# Types :--- Easy

"""
Problem Statements :-----

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([])"
Output: true

Example 5:

Input: s = "([)]"
Output: false


"""

# Code :---


def isValid(str):

    stack = []
    match_map = {")": "(", "]": "[", "}": "{"}

    for curr in str:

        if curr in match_map:

            if not stack or stack.pop() != match_map[curr]:
                return False

        else:
            stack.append(curr)

    return len(stack) == 0


str = "[]}"
print(isValid(str))
