class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p=head
        if p is None:
            return p
        while p.next is not None:
            if p.val==p.next.val:
                p.next=p.next.next
            else:
                p=p.next
        return head    
