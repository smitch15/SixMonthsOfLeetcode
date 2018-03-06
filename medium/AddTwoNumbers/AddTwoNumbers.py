# Steven Mitchell
# 185DaysOfCode
# Problem 2 - 3/2/18

"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
"""


# Definition for singly-linked list.
# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None
#
# 	def __str__(self):
# 		count = 0
# 		outStr = ""
# 		while (self.next != None):
# 			outStr += "node: " + str(count) + ", val: " + str(self.val)+'\n'
# 			self = self.next
# 			count += 1
# 		outStr += "node: " + str(count) + ", val: " + str(self.val)+'\n'
# 		return outStr



class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = l1
        head2 = l2
        carry = 0
        while (head1.next != None and head2.next != None):
            head1.val = head1.val + head2.val + carry
            if (head1.val >= 10):
                rem = head1.val % 10
                head1.val  = rem
                carry = 1
            else:
                carry = 0
            head1 = head1.next
            head2 = head2.next
        if (head1.next == None and head2.next != None):
            head1.val = head1.val + head2.val + carry
            head1.next = head2.next
            while (head1.val >= 10):
                if (head1.next == None):
                    head1.val = head1.val % 10
                    head1.next = ListNode(1)
                else:
                    head1.val = head1.val % 10
                    head1.next.val += 1
                    head1 = head1.next
            return l1
        elif (head1.next != None and head2.next == None):
            head1.val = head1.val + head2.val + carry
            while (head1.val >= 10):
                if (head1.next == None):
                    head1.val = head1.val % 10
                    head1.next = ListNode(1)
                else:
                    head1.val = head1.val % 10
                    head1.next.val += 1
                    head1 = head1.next
            return l1
        else: # head1.next and 2.next are None
            head1.val = head1.val + head2.val + carry
            if (head1.val >= 10):
                head1.val = head1.val % 10
                head1.next = ListNode(1)
            return l1

# def main():
# 	s1 = Solution()
# 	# add 99 and 1 == 100
# 	l1 = ListNode(1)
# 	l2 = ListNode(9)
# 	l3 = ListNode(9)
# 	l2.next = l3
# 	print(s1.addTwoNumbers(l1, l2))
#
#
# main()
