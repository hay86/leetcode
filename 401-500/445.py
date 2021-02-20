# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2 = 0, 0
        p1, p2 = l1, l2
        while p1:
            p1 = p1.next
            s1 += 1
        while p2:
            p2 = p2.next
            s2 += 1
        if s1 < s2:
            s1, s2 = s2, s1
            l1, l2 = l2, l1
        for i in range(s1 - s2 + 1):
            l3 = ListNode(0)
            l3.next = l2
            l2 = l3
        prev = l2
        p1, p2 = l1, l2.next
        v0, c9 = prev.val, 0
        for i in range(s1):
            v = p1.val + p2.val
            if v == 9:
                c9 += 1
            elif v < 9:
                prev.val = v0
                prev = prev.next
                while c9 > 0:
                    prev.val = 9
                    prev = prev.next
                    c9 -= 1
                v0 = v
            else:
                prev.val = v0 + 1
                prev = prev.next
                while c9 > 0:
                    prev.val = 0
                    prev = prev.next
                    c9 -= 1
                v0 = v % 10
            p1 = p1.next
            p2 = p2.next
        prev.val = v0
        prev = prev.next
        while c9 > 0:
            prev.val = 9
            prev = prev.next
            c9 -= 1
        if l2.val == 0:
            l2 = l2.next
        return l2
