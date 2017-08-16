# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        m = 0
        p = head
        while p is not None:
            m += 1
            p = p.next
        if m == 0 or n <= 0:
            return head
        if n == m:
            head = head.next
        elif n < m:
            m -= (n+1)
            p = head
            while m > 0:
                p = p.next
                m -= 1
            p.next = p.next.next
        return head
