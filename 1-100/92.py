# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        fake = ListNode(0)
        fake.next = head
        head = fake
        p0 = head
        cnt = 0
        while p0 is not None and cnt < m-1:
            p0 = p0.next
            cnt += 1
        p1, p2 = None, p0.next
        for i in range(n-m+1):
            tmp = p2.next
            p2.next = p1
            p1, p2 = p2, tmp
        if p0.next is not None:
            p0.next.next = p2
        p0.next = p1
        return fake.next
