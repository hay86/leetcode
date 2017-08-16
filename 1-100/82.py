# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        tmp = ListNode(0)
        tmp.next = head
        head = tmp
        val = tmp.next.val
        cnt = 1
        tmp = tmp.next
        valid = head
        while tmp.next is not None:
            if tmp.next.val == val:
                cnt += 1
            else:
                if cnt == 1:
                    valid.next = tmp
                    valid = tmp
                val = tmp.next.val
                cnt = 1
            tmp = tmp.next
        if cnt > 1:
            valid.next = None
        else:
            valid.next = tmp
        return head.next
                
