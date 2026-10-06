# Questions :---- 101. Symmetric Tree

"""

Problem Statements :---

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true


Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false


"""

# Code :----
from collections import isMirror


def isSymmetric(root):
    if not root:
        return True

    return isMirror(root.left, root.right)


def isMirro(self, t1, t2):
    if t1 is None and t2 is None:
        return True

    if t1 is None or t2 is None:
        return False

    if t1.val != t2.val:
        return False

    return self.isMirror(t1.left, t2.left) and self.isMirror(t1.right, t2.right)
