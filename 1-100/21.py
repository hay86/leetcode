# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = None
        if l1 is None and l2 is not None:
            ret = l2
        elif l1 is not None and l2 is None:
            ret = l1
        elif l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                ret = ListNode(l1.val)
                l1 = l1.next
            else:
                ret = ListNode(l2.val)
                l2 = l2.next
            tail = ret
            while l1 is not None and l2 is not None:
                if l1.val <= l2.val:
                    tail.next = ListNode(l1.val)
                    l1 = l1.next
                    tail = tail.next
                else:
                    tail.next = ListNode(l2.val)
                    l2 = l2.next
                    tail = tail.next
            while l1 is not None:
                tail.next = ListNode(l1.val)
                l1 = l1.next
                tail = tail.next
            while l2 is not None:
                tail.next = ListNode(l2.val)
                l2 = l2.next
                tail = tail.next
        return ret
