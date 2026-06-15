# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next

        rem = head
        for i in range(l//2):
            rem = rem.next
        second = rem.next
        rem.next = None

        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        f = head
        s = prev

        while s:
            tmp1 = f.next
            tmp2 = s.next

            f.next = s
            s.next = tmp1
            
            f = tmp1
            s = tmp2
        
        
            

        