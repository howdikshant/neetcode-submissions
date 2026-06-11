# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = head1
        curr2 = head2
        res = ListNode(0)
        add1 = 0
        add2 = 0
        i = 0
        while curr1:
            add1 += curr1.val * 10**i
            i += 1
            curr1 = curr1.next
        i = 0
        while curr2:
            add2 += curr2.val * 10**i
            i += 1
            curr2 = curr2.next       
        s = add1 + add2
        
        digits = [int(d) for d in str(s)[::-1]]
        curr = res
        for d in digits:
            curr.next = ListNode(d)
            curr = curr.next    
        return res.next





