# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        current_node = head
        
        # Iterating over all the available nodes
        while current_node and current_node.next:
			# Keep a next of the head's next node
            temporary_node = current_node.next.next
            
            # If a value is equal, set a next node of the head's next node
            if current_node.val == current_node.next.val:
                current_node.next = temporary_node
            
            # Otherwise, just keep iterating over the LinkedList
            else:
                current_node = current_node.next
        return head
        