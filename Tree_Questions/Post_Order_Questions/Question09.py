# Questions :-----  124. Binary Tree Maximum Path Sum

"""
Problem Statements :---

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.


Example 2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

"""

# Code :---


def maxPathSum(self, root):
    self.max_sum = float("-inf")

    def calculate_max_gain(node):
        if node is None:
            return 0

        left_gain = max(calculate_max_gain(node.left), 0)
        right_gain = max(calculate_max_gain(node.right), 0)

        currect_max_path = node.val + left_gain + right_gain
        self.max_sum = max(self.max_sum, currect_max_path)
        return node.val + max(left_gain, right_gain)

    calculate_max_gain(root)
    return self.max_sum
