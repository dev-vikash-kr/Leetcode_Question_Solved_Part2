# Questions :----  217. Contains Duplicate
# types :-- Easy Types
"""
Problem Statement :--- Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

# Code :---


def containDuplicate(nums):
    hashset = set()

    for i in nums:
        if i in hashset:
            return True

        hashset.add(i)

    return False


nums = [1, 2, 3, 4]
print(
    containDuplicate(nums)
)  # It output give as False because given a number of value is not duplicate and it is distinct type so that thye are give us False in output.


def containDupicate(nums):
    hashset = set()

    for i in nums:
        if i in hashset:
            return True

        hashset.add(i)

    return False


nums = [1, 2, 3, 3, 4]
print(
    containDupicate(nums)
)  # it output give as True becuase given a number of value is duplicate and it is not distinct type so that they are give us True in output.
