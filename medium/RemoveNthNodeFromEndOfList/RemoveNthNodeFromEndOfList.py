"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if (n==0):
            return head
        if (head.next == None):
            if (n == 1):
                return None
            return head
        nth = head
        last = head
        while (last.next):
            if (n > 0):
                last = last.next
                n -= 1
            else:
                last = last.next
                nth = nth.next
        if (nth.next == last):
            nth.next = None
            return head
        if (nth == head):
            return nth.next

        
        nth.next = last
        return head

