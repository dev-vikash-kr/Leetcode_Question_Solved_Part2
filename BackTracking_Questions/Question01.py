# Questions :----- 46. Permutations

"""
Problems Statements :----

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]


Example 3:

Input: nums = [1]
Output: [[1]]


"""

# Code :----


def permute(nums):
    result = []

    def backtrack(index):
        if index == len(nums):
            result.append(nums[:])
            return

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            backtrack(index + 1)
            nums[index], nums[i] = nums[i], nums[index]

    backtrack(0)
    return result


nums = [1, 2, 3]

print(permute(nums))
