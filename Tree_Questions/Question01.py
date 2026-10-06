# Questions :--- 102. Binary Tree Level Order Traversal

"""
Problem Statements :----

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]


Example 2:

Input: root = [1]
Output: [[1]]


Example 3:

Input: root = []
Output:

"""

# Code :----


def levelOrder(root):
    result = []

    def dfs(node, depth):
        if not node:
            return

        if depth == len(result):
            result.append([])

        result[depth].append(node.val)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)

    return result

