/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var added, num, carry int
    
    mylist := &ListNode{0, nil}
    dummy := mylist
    
    // loop over the two list
    for ;l1 != nil && l2 != nil; l1, l2 = l1.Next, l2.Next {
        added = l1.Val + l2.Val + carry
        num, carry = added % 10, added / 10
        
        mylist.Next = &ListNode{num, nil}
        mylist = mylist.Next
    }
    
    // loop over one list
    for ;l1 != nil; l1 = l1.Next {
        added = l1.Val + carry
        num, carry = added % 10, added / 10
        
        mylist.Next = &ListNode{num, nil}
        mylist = mylist.Next
    }
    
    for ;l2 != nil; l2 = l2.Next {
        added = l2.Val + carry
        num, carry = added % 10, added / 10
        
        mylist.Next = &ListNode{num, nil}
        mylist = mylist.Next
    }
    
    // don't forget the carry baby!
    if carry != 0 {
        mylist.Next = &ListNode{carry, nil}
        mylist = mylist.Next
    }
    
    return dummy.Next
    
}