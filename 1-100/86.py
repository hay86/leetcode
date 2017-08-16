# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.val >= x:
            p = head
            while p.next is not None and p.next.val >= x:
                p = p.next
            if p.next is not None:
                q = p.next
                p.next = q.next
                q.next = head
                head = q
        tail = head
        p = head
        while p.next is not None:
            if p.next.val < x:
                if tail != p:
                    q = p.next
                    p.next = q.next
                    q.next = tail.next
                    tail.next = q
                    tail = q
                else:
                    tail = tail.next
                    p = p.next
            else:
                p = p.next
        return head
