# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        p = head
        while p.next is not None:
            if head.val >= p.next.val:
                k = p.next
                p.next = k.next
                k.next = head
                head = k
            elif p.val <= p.next.val:
                p = p.next
            else:
                q = head
                while q != p and q.next.val < p.next.val:
                    q = q.next
                if q != p:
                    k = p.next
                    p.next = k.next
                    k.next = q.next
                    q.next = k
                else:
                    p = p.next
        return head
