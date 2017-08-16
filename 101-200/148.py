# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        end = head
        while end.next is not None:
            end = end.next
        l, r = self.sort(head, end)
        return l
            
    def sort(self, start, end):
        if start == end:
            return start, end
        if start.next == end:
            if start.val > end.val:
                tmp = start.val
                start.val = end.val
                end.val = tmp
            return start, end
        p1 = start
        p2 = start
        while p2.next != end and p2.next.next != end:
            p1 = p1.next
            p2 = p2.next.next
        l1, r1 = self.sort(start, p1)
        l2, r2 = self.sort(r1.next, end)
        r1.next = l2
        if l1.val > l2.val:
            r1.next = l2.next
            l2.next = l1
            l1 = l2
        s, e = l1, r1
        while s != e:
            if s.next.val > e.next.val:
                tmp = e.next
                e.next = tmp.next
                tmp2 = s.next
                s.next = tmp
                tmp.next = tmp2
                if tmp == r2:
                    r2 = e
                    break
            s = s.next
        return l1, r2
    
    def xxx(self, s, e):
        while s != e:
            print s.val,
            s = s.next
        print e.val
                
