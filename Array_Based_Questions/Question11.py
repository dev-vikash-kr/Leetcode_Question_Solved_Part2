# Questions :--- 977. Squares of a Sorted Array

"""
Problem Statements:---

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].


Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


"""

# Code :--


def sortedSquare(nums):
    result = []
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] * nums[left] > nums[right] * nums[right]:
            result.append(nums[left] * nums[left])
            left += 1

        else:
            result.append(nums[right] * nums[right])
            right -= 1

    return result[::-1]


num = [9, -1, 5, -10, 10, -25]
print(sortedSquare(num))
