# Questions :-----  1480. Running Sum of 1d Array

"""
Problem Statements :---

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.


Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


"""

# Code :--

# Brute Froce  approach -------------

def runningSum(nums):
    result = []

    for i in range(len(nums)):
        total = 0

        for j in range(i + 1):
            total += nums[j]

        result.append(total)

    return result


num = [1, 2, 4]
print(runningSum(num))


# Optimal Approach :---------------


def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]

    return nums


num = [1, 2, 4]
print(runningSum(num))
