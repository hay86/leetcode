import bisect
class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.rdata = {}
        self.val = []

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.data:
            self.rdata[self.data[key]].remove(key)
            if len(self.rdata[self.data[key]]) == 0:
                del self.rdata[self.data[key]]
                self.valRm(self.data[key])
            self.data[key] += 1
            if self.data[key] in self.rdata:
                self.rdata[self.data[key]].add(key)
            else:
                self.rdata[self.data[key]] = {key}
                self.valAdd(self.data[key])
        else:
            self.data[key] = 1
            if 1 in self.rdata:
                self.rdata[1].add(key)
            else:
                self.rdata[1] = {key}
                self.valAdd(1)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.data:
            if self.data[key] <= 1:
                self.rdata[1].remove(key)
                if len(self.rdata[1]) == 0:
                    del self.rdata[1]
                    self.valRm(1)
                del self.data[key]
            else:
                self.rdata[self.data[key]].remove(key)
                if len(self.rdata[self.data[key]]) == 0:
                    del self.rdata[self.data[key]]
                    self.valRm(self.data[key])
                self.data[key] -= 1
                if self.data[key] in self.rdata:
                    self.rdata[self.data[key]].add(key)
                else:
                    self.rdata[self.data[key]] = {key}
                    self.valAdd(self.data[key])

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if len(self.val) == 0:
            return ''
        else:
            for x in self.rdata[self.val[-1]]:
                break
            return x

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if len(self.val) == 0:
            return ''
        else:
            for x in self.rdata[self.val[0]]:
                break
            return x
        
    def valAdd(self, v):
        self.val.insert(bisect.bisect(self.val, v), v)
        
    def valRm(self, v):
        self.val.remove(v)

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
