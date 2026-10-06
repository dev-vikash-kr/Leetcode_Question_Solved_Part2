# Questions :-- 662. Maximum Width of Binary Tree

"""
Problem Statements :-----

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.


Example 1 :-----


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

"""

# Code :----------


def widthOfBinaryTree(root):
    max_width = 0
    leftmost_indices = []

    def dfs(node, depth, index):
        nonlocal max_width
        if not node:
            return

        if depth == len(leftmost_indices):
            leftmost_indices.append(index)

        widht = index - leftmost_indices[depth] + 1
        max_width = max(max_width, widht)

        normalized_index = index - leftmost_indices[depth]
        dfs(node.left, depth + 1, 2 * normalized_index)
        dfs(node.right, depth + 1, 2 * normalized_index + 1)

    dfs(root, 0, 0)
    return max_width
