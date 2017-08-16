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
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        tmp = l1.val + l2.val
        head = ListNode(tmp%10)
        carry = tmp/10
        l1 = l1.next
        l2 = l2.next
        tail = head
        while l1 is not None and l2 is not None:
            tmp = l1.val + l2.val + carry
            tail.next = ListNode(tmp%10)
            carry = tmp/10
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        l = l1 if l2 is None else l2
        while l is not None and carry == 1:
            tmp = l.val + carry
            tail.next = ListNode(tmp%10)
            carry = tmp/10
            tail = tail.next
            l = l.next
        if l is not None:
            tail.next = l
        elif carry == 1:
            tail.next = ListNode(1)
        return head
        
