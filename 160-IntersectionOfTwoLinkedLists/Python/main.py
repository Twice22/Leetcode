# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # we can do it in 2 passes.
        # first pass we recover the length of list1 and list2
        # then from their we deduce the difference between
        # list1 and list2.
    
        # if list2 - list1 = n > 0 then list2 is longer than
        # list1 and we do another pass but this time we give list2
        # a head start of n steps. When we iterate through list1 and list2
        # all together. Once element in list1 matches element in list2
        # we return the node.
        
        list1, list2 = headA, headB
        while list1 and list2:
            list1 = list1.next
            list2 = list2.next
        
        n = 0
        isLongerList1 = False
        if list1:
            isLongerList1 = True
            while list1: 
                list1 = list1.next
                n += 1
        if list2:
            while list2:
                list2 = list2.next
                n += 1
        
        longest_list = headA if isLongerList1 else headB
        smallest_list = headA if not isLongerList1 else headB
        
        while n:
            longest_list = longest_list.next
            n -= 1
        
        while longest_list and smallest_list:
            if longest_list == smallest_list:
                return longest_list
            longest_list = longest_list.next
            smallest_list = smallest_list.next