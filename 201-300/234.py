# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        n = 0
        r = head
        while r is not None:
            n += 1
            r = r.next
        m = int(n/2)
        r = head
        while m > 0:
            r = r.next
            m -= 1
        p, q = None, r
        while q is not None:
            r = q.next
            q.next = p
            p = q
            q = r
        q = head
        while p is not None and q is not None:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True
        
            
