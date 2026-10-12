# Questions :--- 1110. Delete Nodes And Return Forest

"""
Problem Statements :----

Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest. You may return the result in any order.

Example 1:

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]

"""

# Code :---


def delNodes(root, to_delete):
    forest = []
    deleteset = set(to_delete)

    def dfs(node, isRoot):
        if not node:
            return None

        shouldDelete = node.val in deleteset
        if isRoot and not shouldDelete:
            forest.append(node)

        node.left = dfs(node.left, shouldDelete)
        node.right = dfs(node.right, shouldDelete)

        return None if shouldDelete else node

    dfs(root, True)
    return forest
