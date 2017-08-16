class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.arr) == 0:
            self.arr.append((x, x))
        else:
            self.arr.append((x, min(x, self.arr[-1][1])))

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.arr) > 0:
            self.arr.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1][0] if len(self.arr) > 0 else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.arr[-1][1] if len(self.arr) > 0 else None
        
