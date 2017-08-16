# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = nestedList
        self.list.reverse()

    def next(self):
        """
        :rtype: int
        """
        return self.ans

    def hasNext(self):
        """
        :rtype: bool
        """
        self.ans = None
        if len(self.list) > 0:
            ret = self.list.pop()
            while not ret.isInteger():
                list2 = ret.getList()
                list2.reverse()
                if len(list2) > 0:
                    ret = list2.pop()
                    self.list.extend(list2)
                elif len(self.list) > 0:
                    ret = self.list.pop()
                else:
                    break
            self.ans = ret.getInteger()
        return self.ans is not None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
