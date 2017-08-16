# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = head
        p2 = p1.next if p1 != None else None
        while p2 != None:
            p1 = p1.next
            p2 = p2.next
            if p2 != None:
                p2 = p2.next
            if p1 == p2:
                break
        if p2 is None:
            return None
        else:
            p3 = p2.next
            c = 1
            while p2 != p3:
                p3 = p3.next
                c += 1
            p1 = head
            p2 = p1
            for i in range(c):
                p2 = p2.next
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1
