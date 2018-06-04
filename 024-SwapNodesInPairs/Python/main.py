# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:     
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mylist = dummy = ListNode(0)
        dummy.next = head
        mylist.next = head
        
        # explanation for 1 -> 2 -> 3 -> 4:
        
        # nex = 1 -> 2 -> 3 -> 4
        # mylist.next = 2 -> 3 ( -> 4) (we invert first node of mylist.next with previous node)
        # nex = 1 -> 3 -> 4
        # mylist.next = 2 -> 1 -> 3 -> 4 (result of dummy.next after first iteration)
        # mylist = 1 -> 3 -> 4
        
        # nex = 3 -> 4
        # mylist.next = 4 (we invert first node of mylist.next with previous node: 3)
        # nex = 3 -> None
        # mylist.next = 4 -> 3 (-> None) (end of result of dummy.next after 2nd iteration)
        # mylist = 3 -> None (end looping)
        
        while mylist.next and mylist.next.next:
            nex = mylist.next
            mylist.next = nex.next
            nex.next = nex.next.next
            mylist.next.next = nex
            mylist = nex
        
        return dummy.next