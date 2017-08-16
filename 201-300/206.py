# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, next = None, head
        while next != None:
            tmp = next.next
            next.next = prev
            prev = next
            next = tmp
        return prev
