# 34. Find First and Last Position of Element in Sorted Array

"""
Problem Statements :----

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""

# Code :----


def searchRange(nums, target):
    first = lower_bound(nums, target)

    if first == len(nums) or nums[first] != target:
        return [-1, -1]

    last = upper_bound(nums, target) - 1
    return [first, last]


def lower_bound(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1

        else:
            right = mid

    return left


def upper_bound(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1

        else:
            right = mid

    return left


nums = [5, 7, 7, 8, 8, 10]
target = 9
print(searchRange(nums, target))
