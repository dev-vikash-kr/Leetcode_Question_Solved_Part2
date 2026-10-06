# Questions :--- 144. Binary Tree Preorder Traversal

"""
Problem Statement: -

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]


"""

# Code :----


def preorderTraversal(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        current = stack.pop()
        result.append(current.val)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return result
