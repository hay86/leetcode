# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p is not None:
            q = p.next
            if q is not None:
                tmp = p.val
                p.val = q.val
                q.val = tmp
            p = p.next
            if p is not None:
                p = p.next
        return head
