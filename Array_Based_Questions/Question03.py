# Questions :---- 217. Contains Duplicate

"""

Problem Statements :---

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



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


# Brute Force :---


def containDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


num = [1, 2, 3, 4, 5]
print(containDuplicate(num))


# Optimals Approach :---


def containDuplicate(nums):
    hashset = set()

    for i in nums:
        if i in hashset:
            return True

        hashset.add(i)

    return False


num = [1, 3, 4, 5, 5]
print(containDuplicate(num))
