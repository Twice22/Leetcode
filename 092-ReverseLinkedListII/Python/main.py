class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # we are sure 1 <= m <= n <= length list
        beg = blist = ListNode(0)
        
        c = 1
        while c < m:
            blist.next = head
            blist = blist.next
            head = head.next
            c += 1
        blist.next = None
        
        prev = None
        current = head
        while c <= n:
            nx = current.next
            current.next = prev
            prev = current
            current = nx
            c += 1
        
        blist.next = prev
        head.next = current
        
        return beg.next