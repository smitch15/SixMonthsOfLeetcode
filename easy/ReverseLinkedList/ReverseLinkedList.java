//Reverse a singly linked list.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        
        if (head == null || head.next == null){
            return head;
        }
        
        ListNode prev = null;
        ListNode curr = head;
        ListNode then = curr.next;
        
        if (then.next == null){
            curr.next = prev;
            then.next = curr;
            return then;
        }
        while(then.next != null){
            curr.next = prev;
            prev = curr;
            curr = then;
            then = curr.next;
        }
        curr.next = prev;
        then.next = curr;
        return then;
    }
}
