class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1:
        start=None
        last=None
        while 1:
            if l2 is None:
                last=l1
            if l1 is None:
                last=l2
            if l1.val<l2.val:
                l=ListNode(l1.val)
                if last is None:
                    last=l
                    start=l
                else :
                    last.next=l
                    last=l
            else:
                l=ListNode(l2.val)
                if last is None:
                    last=l
                    start=l
                else :
                    last.next=l
                    last=l
        return start
