import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.pos = {}
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            self.pos[val].add(self.length)
            ret = False
        else:
            self.pos[val] = set([self.length])
            ret = True
        self.data.append(val)
        self.length += 1
        return ret

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            for p in self.pos[val]:
                break
            self.pos[val].remove(p)
            if len(self.pos[val]) == 0:
                del self.pos[val]
            v = self.data.pop()
            if p != self.length-1:
                self.data[p] = v
                self.pos[v].remove(self.length-1)
                self.pos[v].add(p)
            self.length -= 1
            ret = True
        else:
            ret = False
        return ret

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if self.length > 0:
            return random.choice(self.data)
        return False


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
