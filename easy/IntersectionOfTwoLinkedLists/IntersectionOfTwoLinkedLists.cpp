/**
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
**/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// Time Complexity: O(n)
// real clever solution: if you add the lengths of both lists
// they will traverse the same distance until right before the 
// intersection. A.length = a + c; B.length = b + c; --> a+c+b == b+c+a
// A.length == B.length --> both traverse a+c+b nodes, next node is the
// start of the intersection
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *pa = headA;
        ListNode *pb = headB;
        if (headA == nullptr || headB == nullptr)   return nullptr;
        while(pa!=nullptr || pb!= nullptr){
            if (pa ==nullptr)    pa = headB;
            if (pb == nullptr)   pb = headA;
            if (pa == pb)   return pa;
            pa = pa->next;
            pb = pb->next;
        }
        return nullptr;
    }
};
        

// Time Complexity: O(n^2)
/**
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *firstB = headB;
        while (headA != nullptr){
            while(headB != nullptr){
                if (headA == headB){
                    return headA;
                }
                headB = headB->next;
            }
            headB = firstB;
            headA = headA->next;
        }
        return nullptr;
    }
};
**/
