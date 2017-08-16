import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.pos = {}
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        self.data.append(val)
        self.pos[val] = self.length
        self.length += 1
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False
        v = self.data.pop()
        if v != val:
            p = self.pos[val]
            self.data[p] = v
            self.pos[v] = p
        del self.pos[val]
        self.length -= 1
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.length > 0:
            return random.choice(self.data)
        return False


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
