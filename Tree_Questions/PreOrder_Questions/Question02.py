# Questions :--- 100. Same Tree

"""

Problem Statements :------

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false


Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false


"""

# Code :----


def issameTree(self, p, q, val=0):
    self.val = val
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val:
        return False

    return issameTree(p.left, q.left) and issameTree(p.right, q.right)


p = [1, 2, 3]
q = [1, 2, 3]
print(issameTree(p, q,))
