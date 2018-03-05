### Reverse a singly linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None or head.next == None):
            return head
        prev = None
        curr = head
        then = curr.next
        if (then.next == None):
            curr.next = prev
            then.next = curr
            return then
        while(then.next != None):
            curr.next = prev
            prev = curr
            curr = then
            then = curr.next
        curr.next = prev
		then.next = curr
        return then
