class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []
        self.b = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        while len(self.b) > 0:
            self.a.append(self.b.pop())
        self.b.append(x)
        while len(self.a) > 0:
            self.b.append(self.a.pop())

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.b) > 0:
            self.b.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.b) > 0:
            return self.b[-1]
        return None

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.b) == 0
        
