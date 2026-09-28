# Questions :----109. Convert Sorted List to Binary Search Tree

"""
Problem Statement :----

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

"""

# Code :---


def sortedListToBST(self, ListNode, head, TreeNode):
    if not head:
        return None
        if not head.next:
            return TreeNode(head.val)

        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root


head = [-10, -3, 0, 5, 9]
print(sortedListToBST(head))
