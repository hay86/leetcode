# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        head2 = RandomListNode(head.label)
        tmp1, tmp2 = head, head2
        m = {head:head2}
        while tmp1.next is not None:
            tmp2.next = RandomListNode(tmp1.next.label)
            tmp1, tmp2 = tmp1.next, tmp2.next
            m[tmp1] = tmp2
        tmp1, tmp2 = head, head2
        while tmp1.next is not None:
            if tmp1.random is not None:
                tmp2.random = m[tmp1.random]
            tmp1, tmp2 = tmp1.next, tmp2.next
        if tmp1.random is not None:
            tmp2.random = m[tmp1.random]
        return head2
        
