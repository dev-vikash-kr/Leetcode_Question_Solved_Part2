# Questions :--- 103. Binary Tree Zigzag Level Order Traversal

"""
Problem statements :----

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

"""

# Code :----

from collections import deque


def zigZagLevelOrder(root):
    result = []

    def dfs(node, depth):
        if not node:
            return

        if depth == len(result):
            result.append(deque())

        if depth % 2 == 0:
            result[depth].append(node.val)

        else:
            result[depth].appendleft(node.val)

        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return [list(l) for l in result]


# TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Create the tree
root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


# Call your function
print(zigZagLevelOrder(root))
