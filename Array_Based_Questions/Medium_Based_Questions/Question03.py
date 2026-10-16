# Questions :--  560. Subarray Sum Equals K

"""
Problem Statements :--

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

"""

# Code :---


# def subarraySum(nums, k):
#     count = 0
#     sum = 0
#     prefix_count = {0: 1}

#     for num in nums:
#         sum += num
#         count += prefix_count.get(sum - k, 0)
#         prefix_count[sum] = prefix_count.get(sum, 0) + 1

#     return count


# num = [1, 1, 1]
# k = 2

# print(subarraySum(num, k))


def subarraySub(nums, k):

    count = 0
    sum = 0
    prefix_count = {0: 1}

    for num in nums:
        sum += num
        count += prefix_count.get(sum - k, 0)
        prefix_count[sum] = prefix_count.get(sum, 0) + 1

    return count


num = [1, 1, 1]
k = 2
print(subarraySub(num, k))
