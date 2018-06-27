# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # (1): if k == 0 directly return the input list head
        if k == 0:
            return head
        
        beg = lst = head
        
        # length of the list
        size = 0
        while head:
            size += 1
            if head.next == None:
                # get the last node
                end = head
            head = head.next
        
        # we do the modulo just after so we first need to ensure size != 0
        if size == 0 or size == 1:
            return beg
        
        # rotate by (modulo)
        k = k % size
        
        # same case as (1) but doesn't handle by 1 because of modulo
        if k == 0:
            return beg
        
        start_at = size - k
        
        c = 1
        while c < start_at:
            lst = lst.next
            c += 1
        
        res = lst.next # link node at pos size - k
        lst.next = None # node at position size -k point to None
        end.next = beg # finally can pt end to beg to loop without fearing infinite loop
              
        return res