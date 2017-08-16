# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        return self.sortedArrayToBST(arr, 0, len(arr)-1)
        
    def sortedArrayToBST(self, arr, l, r):
        if l > r:
            return None
        m = int((l+r)/2)
        root = TreeNode(arr[m])
        root.left = self.sortedArrayToBST(arr, l, m-1)
        root.right = self.sortedArrayToBST(arr, m+1, r)
        return root
