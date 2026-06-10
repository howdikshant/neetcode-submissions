# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = head1
        curr2 = head2
        dummy = ListNode(0)
        tail = dummy
        while curr1 and curr2:
            if curr1.val >= curr2.val:
                tail.next = curr2
                curr2 = curr2.next
                tail = tail.next
            elif curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
                tail = tail.next
        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2
        return dummy.next

