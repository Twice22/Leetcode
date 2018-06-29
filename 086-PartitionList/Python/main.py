# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        # Warning: Need to define ListNode(0)
        # for inf and ListNode(0) for sup
        # we CANNOT do:
        # inf_list = sup_list = ListNode(0)
        # beg_sup_list = sup_list
        # beg_inf_list = inf_list
        inf_list = beg_inf_list = ListNode(0)
        sup_list = beg_sup_list = ListNode(0)
        
        while head:
            if head.val < x:
                inf_list.next = head
                inf_list = head # inf_list.next
            else:
                sup_list.next = head
                sup_list = head # sup_list.next
            head = head.next
        
        sup_list.next = None
        inf_list.next = beg_sup_list.next
        
        return beg_inf_list.next
        
        