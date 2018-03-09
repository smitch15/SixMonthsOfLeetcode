"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first = head
        second = head
        while(first and second):
            if (second.next == None or first.next == None):
                return False
            first = first.next
            second = second.next.next
            if (first == second):
                return True
        return False
