# Questions :--- 257. Binary Tree Paths

"""
Problem Statements :----

You are given the root of a binary tree.

Return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]


Example 2:

Input: root = [1]
Output: ["1"]

"""

# Code :---


def binaryTreePaths(root):
    if not root:
        return []

    paths = []
    stack = [(root, str(root.val))]
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            paths.append(path)

        else:
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))

            if node.left:
                stack.append((node.left, path + "->" + str((node.left.val))))

    return paths
