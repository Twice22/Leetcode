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
        
        res = head
        
        while head:
            v = head.val
            bef = head
            head = head.next
            while head and head.val == v:
                head = head.next
            bef.next = head
        
        return res
            