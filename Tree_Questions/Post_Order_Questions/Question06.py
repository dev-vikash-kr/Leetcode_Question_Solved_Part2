# Questions :----- 652. Find Duplicate Subtrees

"""
Problem Statements :---

Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.

Example 1:

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]


Example 2:

Input: root = [2,1,1]
Output: [[1]]

Example 3:

Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

"""

# Code :---


def findDuplicateSubTree(self, root):
    self.id = 1
    self.tree = {}
    self.count = {}
    self.result = []
    self.lookup(root)
    return self.result


def lookup(self, root):
    if not root:
        return 0

    serial = f"{root.val}, {self.lookup(root.left)},{self.lookup(root.right)}"

    if serial not in self.trees:
        self.tress[serial] = self.id
        self.id += 1

    tree_id = self.trees[serial]

    self.count[tree_id] = self.count.get(tree_id, 0) + 1

    if self.count[tree_id] == 2:
        self.result.append(root)

    return tree_id
