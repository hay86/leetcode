# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        sizeA, sizeB = 0, 0
        endA = headA
        while endA.next is not None:
            endA = endA.next
            sizeA += 1
        endB = headB
        while endB.next is not None:
            endB = endB.next
            sizeB += 1
        if endA != endB:
            return None
        if sizeA > sizeB:
            for i in range(sizeA-sizeB):
                headA = headA.next
        elif sizeA < sizeB:
            for i in range(sizeB-sizeA):
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
