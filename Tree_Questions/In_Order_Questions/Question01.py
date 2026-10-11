# Questions :----- 94.Binary Tree Inorder Traversal.

"""
Problem Statements :---

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]
Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]

Explanation:

Example 3:

Input: root = []
Output: []

Example 4:

Input: root = [1]
Output: [1]


"""

# Code :---


def inorderTrversal(root):
    result = []
    curr = root

    while curr:
        if not curr.left:
            result.append(curr.val)
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
                result.append(curr.val)
                curr = curr.right
    return result
