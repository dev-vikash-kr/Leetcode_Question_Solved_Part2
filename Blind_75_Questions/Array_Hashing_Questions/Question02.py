# Questions :---  219.Contains Duplicate II
# Types :------ Easy
"""
Problem Statements :----

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false


"""

# Code :----


def containsNearDuplicate(nums, k):
    map = {}

    for i, nums in enumerate(nums):
        if nums in map:
            if i - map[nums] <= k:
                return True

        map[nums] = i

    return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
print(
    containsNearDuplicate(nums, k)
)  # It code return output False becasue the number and absulate value not equal or less then to k .


def containsNearDuplicates(nums, k):
    map = {}

    for i, nums in enumerate(nums):
        if nums in map:
            if i - map[nums] <= k:
                return True

        map[nums] = i

    return False


nums = [1, 2, 3, 1]
k = 3

print(containsNearDuplicates(nums, k))

