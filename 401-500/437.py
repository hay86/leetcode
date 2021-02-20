# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.ret = 0
        if root != None:
            self.dfs(root, 0, sum, {})
        return self.ret
    
    def dfs(self, root, val, sum, mem):
        val += root.val
        if val == sum:
            self.ret += 1
        if val-sum in mem:
            self.ret += mem[val-sum]
        if val in mem:
            mem[val] += 1
        else:
            mem[val] = 1
        if root.left != None:
            self.dfs(root.left, val, sum, mem)
        if root.right != None:
            self.dfs(root.right, val, sum, mem)
        if mem[val] > 1:
            mem[val] -= 1
        else:
            del mem[val]
