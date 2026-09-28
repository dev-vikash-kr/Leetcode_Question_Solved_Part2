# Questions :---21. Merge Two Sorted Lists

"""

Problem Statement :--- You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [], list2 = []
Output: []

Example 2:
Input: list1 = [], list2 = [0]
Output: [0]

"""

# Code :---


# def mergeTwoList(self, list1, list2):
#     if not list1:
#         return list2
#     if not list2:
#         return list

#     if list1.val <= list2.val:
#         list1.next = self.mergeTwoList(list1.next, list2)
#         return list1

#     else:
#         list2.next = self.twomergeTwoList(list1.next, list2)
#         return list2


def mergeTwoLists(self, list1, list2, ListNode):

    dummy = ListNode(0)
    tail = dummy

    # Compare heads and attach the smaller node
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Attach whichever list still has remaining nodes
    tail.next = list1 if list1 else list2

    return dummy.next


list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(mergeTwoLists(list1, list2))

