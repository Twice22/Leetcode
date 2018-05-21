# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """        
        added, num, carry = 0, 0, 0
        
        # initialize ListNode
        dummy = mylist = ListNode(0)
        
        # browse lists
        while l1 != None and l2 != None:
            added = l1.val + l2.val + carry
            num, carry = added % 10, added // 10
            
            mylist.next = ListNode(num)
            mylist = mylist.next
            l1, l2 = l1.next, l2.next
        
        # browse only one list of the 2 list
        while l1 != None: # and l2.next == None
            added = l1.val + carry
            num, carry = added % 10, added // 10
            mylist.next = ListNode(num)
            mylist = mylist.next
            
            l1 = l1.next
            
        # browse only one list of the 2 list
        while l2 != None: # and l1.next == None            
            added = l2.val + carry
            num, carry = added % 10, added // 10
            mylist.next = ListNode(num)
            mylist = mylist.next
            
            l2 = l2.next
            
        # take care of the carry
        if carry != 0:
            mylist.next = ListNode(carry)
            mylist = mylist.next
            
        return dummy.next