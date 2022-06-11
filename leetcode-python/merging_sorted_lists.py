class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p=list1
        q=list2
        tail=ListNode(0)
        dummy=tail
        while p and q:
            if p.val<q.val:
                dummy.next=p
                p=p.next
            else:
                dummy.next=q
                q=q.next
            dummy=dummy.next
        if p:
            dummy.next=p
            p=p.next
        if q:
            dummy.next=q
            q=q.next
            
        return tail.next