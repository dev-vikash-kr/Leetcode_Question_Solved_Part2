# Questions :---- 493. Reverse Pairs

"""

Problem Statements :---

Given an integer array nums, return the number of reverse pairs in the array.
A reverse pair is a pair (i, j) where:
0 <= i < j < nums.length and
nums[i] > 2 * nums[j].

Example 1:
Input: nums = [1,3,2,3,1]
Output: 2

Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

Example 2:
Input: nums = [2,4,3,5,1]

Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

"""

# Code :------

import math


class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        n = len(nums)

        # Collect all values and thresholds for coordinate compression
        all_vals_clean = set()
        for x in nums:
            all_vals_clean.add(x)
            all_vals_clean.add(int(math.floor((x - 1) / 2)))

        # Build compressed index map
        sorted_vals = sorted(all_vals_clean)
        compress = {v: i + 1 for i, v in enumerate(sorted_vals)}

        size = len(sorted_vals)
        bit = [0] * (size + 1)

        def update(index):
            while index <= size:
                bit[index] += 1
                index += index & (-index)

        def query(index):
            total = 0
            while index > 0:
                total += bit[index]
                index -= index & (-index)
            return total

        count = 0
        # Process from right to left
        for i in range(n - 1, -1, -1):
            threshold = int(math.floor((nums[i] - 1) / 2))
            # Count elements seen so far that are <= threshold
            count += query(compress.get(threshold, 0))
            # Insert current element
            update(compress[nums[i]])

        return count
