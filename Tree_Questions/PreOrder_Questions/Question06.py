# Questions :---- 222. Count Complete Tree Nodes

"""
Problem Statements :---

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:

Input: root = []
Output: 0

Example 3:

Input: root = [1]
Output: 1


"""

# Code :---


def countNode(root):
    if root is None:
        return 0

    lh = leftHeight(root)
    rh = rightHeight(root)
    if lh == rh:
        return (1 << lh) - 1

    return 1 + countNode(root.left) + countNode(root.right)
  

def leftHeight(node):
    h = 0
    while node:
        h += 1
        node = node.left
    return h


def rightHeight(node):

    h = 0
    while node:
        h += 1
        node = node.right

    return h
