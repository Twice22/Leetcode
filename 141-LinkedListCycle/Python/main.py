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
        # classic, just use 2 pointer (one fast and one slow)
        
        ptr1 = head
        
        if head:
            ptr2 = head.next
        else:
            return False
        
        if ptr1 == ptr2:
            return True
        
        while ptr1 and ptr2:
            ptr1 = ptr1.next
            if (ptr2.next):
                ptr2 = ptr2.next.next
            else:
                ptr2 = ptr2.next
            
            if ptr1 == ptr2:
                return True
        
        return False