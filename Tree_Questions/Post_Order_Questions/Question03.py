# Questions :--- 543. Diameter of Binary Tree

"""
Problem Statements :---

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].


Example 2:

Input: root = [1,2]
Output: 1

"""

# Code :---


def diameterOfBinaryTree(self, root):
    self.max_diameter = 0

    def calculate_height(node):
        if node is None:
            return 0

        left_height = calculate_height(node.left)
        right_height = calculate_height(node.right)

        diameter_through_node = left_height + right_height
        self.max_diameter = max(self.max_diameter, diameter_through_node)

        return 1 + max(left_height, right_height)

    calculate_height(root)
    return self.max_diameter
