# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        size = 0
        r, tail = head, None
        while r is not None:
            tail = r
            r = r.next
            size += 1
        k = k % size
        if k == 0:
            return head
        k = size-k-1
        r = head
        for i in range(k):
            r = r.next
        a, b = r, r.next
        a.next = None
        tail.next = head
        return b
