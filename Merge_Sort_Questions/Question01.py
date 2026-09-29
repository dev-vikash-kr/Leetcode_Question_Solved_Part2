# Questions :---148. Sort List
"""
Problem Statements :----

Given the head of a linked list, return the list after sorting it in ascending order.

Example 1 :--

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2 :---

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3 :----

Input: head = []
Output: []

"""

# Code :----


def sortList(self, head, ListNode):
    if not head or not head.next:
        return head

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    right_head = slow.next
    slow.next = None

    left = self.sortList(head)
    right = self.sortList(right_head)

    return self.merge(left, right)


def merge(self, l1, l2, ListNode):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l1.val:
            current.next == l1
            l1 = l1.next

        else:
            current.next = l2
            l2 = l2.next

            current = current.next

    current.next = l1 if l1 else l2

    return dummy.next
