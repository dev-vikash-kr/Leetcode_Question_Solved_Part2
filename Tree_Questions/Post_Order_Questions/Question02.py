# Questions :---- 226. Invert Binary Tree


"""

Problem Statements :-----

Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

"""

# Code :---


def invertTree(root):
    if root is None:
        return None

    stack = [root]

    while stack:
        node = stack.pop()

        temp = node.left
        node.left = node.right
        node.right = temp

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root
