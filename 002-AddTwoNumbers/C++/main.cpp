/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int added = 0, num = 0, carry = 0;
        
        ListNode *mylist = new ListNode(0);
        ListNode *dummy = mylist;
        
        // loop over the two list
        for (; l1 != NULL && l2 != NULL; l1 = l1->next, l2 = l2->next) {
            added = l1->val + l2->val + carry;
            num = added % 10; carry = added / 10;
            
            mylist->next = new ListNode(num);
            mylist = mylist->next;
        }
        
        // loop over one list
        for (; l1 != NULL; l1 = l1->next) {
            added = l1->val + carry;
            num = added % 10; carry = added / 10;
            
            mylist->next = new ListNode(num);
            mylist = mylist->next;
        }
        
        for (; l2 != NULL; l2 = l2->next) {
            added = l2->val + carry;
            num = added % 10; carry = added / 10;
            
            mylist->next = new ListNode(num);
            mylist = mylist->next;
        }
        
        // don't forget the carry
        if (carry != 0) {
            mylist->next = new ListNode(carry);
            mylist = mylist->next;
        }
        
        return dummy->next;
        
    }
};