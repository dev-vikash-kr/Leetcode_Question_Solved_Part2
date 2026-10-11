# Questions :---- 530. Minimum Absolute Difference in BST

"""
Problem Statements :----

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

"""

# Code :---


def getMininumDiff(root):
    curr = root
    prev = None
    min_diff = float("inf")

    while curr:
        if not curr.left:
            if prev is not None:
                min_diff = min(min_diff, curr.val - prev)

            prev = curr.val
            curr = curr.right

        else:
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right

            if not pred.right:
                pred.right = curr
                curr = curr.left
            else:
                pred.right = None
                if prev is not None:
                    min_diff = min(min_diff, curr.val - prev)

                prev = curr.val

                curr = curr.right

    return min_diff
