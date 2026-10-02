# Questions :-- 35. Search Insert Position

"""

Problem Statements :---

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""

# Code :---


def searchInsert(nums, target):

    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1

        else:
            right = mid

    return left


nums = [1, 3, 4, 5]
target = 7

print(searchInsert(nums, target))
