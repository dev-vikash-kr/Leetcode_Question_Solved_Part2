# Questions :--- 4. Median of Two Sorted Arrays

"""
Problem Statements :---

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""

# Code :----


def findMedianSorted(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m = len(nums1)
    n = len(nums2)
    left = 0
    right = m
    half = (m + n + 1) // 2

    while left <= right:
        i = left + (right - left) // 2
        j = half - i

        maxLeft1 = float("-inf") if i == 0 else nums1[i - 1]
        minRight1 = float("inf") if i == m else nums1[i]
        maxLeft2 = float("-inf") if j == 0 else nums2[j - 1]
        minRight2 = float("inf") if j == n else nums2[j]

        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            if (m + n) % 2 == 1:
                return max(maxLeft1, maxLeft2)
            return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2

        elif maxLeft1 > minRight2:
            right = i - 1

        else:
            left = i + 1
    return 0.0


nums1 = [1, 3]
nums2 = [2]

print(findMedianSorted(nums1, nums2))
