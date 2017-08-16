# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1 = head
        p2 = p1.next if p1 != None else None
        while p1 != None and p2 != None:
            p1 = p1.next
            p2 = p2.next
            if p2 != None:
                p2 = p2.next
            if p1 == p2:
                return True
        return False
