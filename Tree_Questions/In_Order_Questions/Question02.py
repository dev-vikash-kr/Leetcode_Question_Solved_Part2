# Questions :------ 783. Minimum Distance Between BST Nodes

"""
Problem Statements :----

Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1


Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

"""

# Code :---


def miniDiffBST(self, root):
    self.min_diff = float("inf")
    self.prev = None

    def inorder(node):
        if not node:
            return

        inorder(node.left)

        if self.prev is not None:
            self.min_diff = min(self.min_diff, node.val - self.prev)
        self.prev = node.val
        inorder(node.right)

    inorder(root)
    return self.min_diff
