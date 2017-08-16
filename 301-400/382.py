
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.cur = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        for i in range(random.randint(0,8)):
            self.cur = self.cur.next
            if self.cur is None:
                self.cur = self.head
        return self.cur.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
