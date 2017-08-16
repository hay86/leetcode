# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return 
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                break
            fast = fast.next
        p, q = None, slow
        while q is not None:
            tmp = q.next
            q.next = p
            p, q = q, tmp
        q = head
        while p is not None and q != p:
            tmp1 = q.next
            tmp2 = p.next
            q.next = p
            if p != tmp1:
                p.next = tmp1
            q, p = tmp1, tmp2
