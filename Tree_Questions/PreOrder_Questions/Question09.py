# Questions :--- 105. Construct Binary Tree from Preorder and Inorder Traversal

"""
Problem Statements :---

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]


Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


"""

# Code :----


def buildTree(preorder, inorder, TreeNode):
    pre_index = 0
    in_index = 0

    def build(stop):
        nonlocal pre_index, in_index
        if pre_index == len(preorder) or inorder[in_index] == stop:
            return None

        root = TreeNode(preorder[pre_index])
        pre_index += 1

        root.index += 1
        root.left = build(root.val)

        in_index += 1
        root.right = build(stop)

        return root

    return build(float("-inf"))
