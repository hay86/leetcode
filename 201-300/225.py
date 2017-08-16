class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        tmp = []
        tmp.append(x)
        for y in self.q:
            tmp.append(y)
        self.q = tmp

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.q) > 0:
            self.q.pop(0)

    def top(self):
        """
        :rtype: int
        """
        if len(self.q) > 0:
            return self.q[0]
        return None

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0
        
