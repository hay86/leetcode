# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None or head.next.next is None:
            return head
        odd, even, head2 = head, head.next, head.next
        i = 1
        node = head.next.next
        while node is not None:
            if i % 2 == 1:
                odd.next = node
                odd = node
            else:
                even.next = node
                even = node
            node = node.next
            i += 1
        even.next = None
        odd.next = head2
        return head
