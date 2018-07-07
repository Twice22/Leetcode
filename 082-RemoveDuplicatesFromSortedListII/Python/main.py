# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(0)
        
        while head:
            nx = head.next
            while nx and head.val == nx.val:
                nx = nx.next
            if nx == head.next:
                prev.next = head
                prev = prev.next
            head = nx
        
        prev.next = None
        return dummy.next
            
        