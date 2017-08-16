# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k<=0:
            return head
        n = 0
        tmp = head
        while tmp is not None:
            tmp = tmp.next
            n += 1
        m = int(n/k)
        tmp = ListNode(0)
        tmp.next = head
        head = tmp
        for i in range(m):
            p1, p2 = None, tmp.next
            for j in range(k):
                tmp2 = p2.next
                p2.next = p1
                p2, p1 = tmp2, p2
            tmp2 = tmp.next
            tmp.next.next = p2
            tmp.next = p1
            tmp = tmp2
        return head.next
