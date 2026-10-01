# Questions :--- 215.Kth Largest Element in an Array.

"""
Problem Statements :----

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


"""

# Code :----


def findKthLargest(nums, k):
    k = len(nums) - k

    def quickSelect(left, right):
        pivot = nums[right]
        p = left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        nums[p], nums[right] = nums[right], nums[p]

        if p > k:
            return quickSelect(left, p - 1)
        elif p < k:
            return quickSelect(p + 1, right)

        else:
            return nums[p]

    return quickSelect(0, len(nums) - 1)


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
# nums = [3, 2, 1, 5, 6, 4]
# k = 2
print(findKthLargest(nums, k))
