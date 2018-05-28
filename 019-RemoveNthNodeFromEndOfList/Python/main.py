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
        dummy = ListNode(0)
        dummy.next = head
        list1 = dummy
        list2 = dummy
        
        # a classic, need 2 pointers
        # we are sure n is valid so no need to check
        for i in range(n):
            list2 = list2.next
        
        while list2.next:
            list1 = list1.next
            list2 = list2.next
        
        list1.next = list1.next.next
        
        return dummy.next
        