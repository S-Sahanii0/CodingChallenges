# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = None
        temp2 = None
        while head:
            temp1 = head.next
            head.next = temp2
            temp2 = head
            head = temp1
        return temp2
        