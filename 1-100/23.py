# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        size = len(lists)
        if size == 0:
            return None
        return self.dc(lists, 0, size-1)
        
    def dc(self, lists, start, end):
        if start == end:
            return lists[start]
        middle = int((start+end)/2)
        a = self.dc(lists, start, middle)
        b = self.dc(lists, middle+1, end)
        if a is None:
            return b
        if b is None:
            return a
        if a.val <= b.val:
            head, tail = a, a
            a = a.next
        else:
            head, tail = b, b
            b = b.next
        while a is not None and b is not None:
            if a.val <= b.val:
                tail.next = a
                tail = a
                a = a.next
            else:
                tail.next = b
                tail = b
                b = b.next
        if a is not None:
            tail.next = a
        elif b is not None:
            tail.next = b
        return head
