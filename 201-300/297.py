# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        q = [root]
        p = [str(root.val)]
        while len(q) > 0:
            node = q.pop(0)
            left, right = node.left, node.right
            if left is not None:
                q.append(left)
            if right is not None:
                q.append(right)
            if len(q) > 0:
                p.append('#' if left is None else str(left.val))
                p.append('#' if right is None else str(right.val))
        return ','.join(p)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        p = data.split(',')
        root = TreeNode(int(p[0]))
        q = [root]
        i, size = 1, len(p)
        while i<size:
            q2 = []
            size2 = 2*len(q)
            for j in range(size2):
                k = i+j
                if k >= size:
                    break
                if p[k] != '#':
                    node = TreeNode(int(p[k]))
                    q2.append(node)
                    if j%2 == 0:
                        q[int(j/2)].left = node
                    else:
                        q[int(j/2)].right = node
            q = q2
            i += size2
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
