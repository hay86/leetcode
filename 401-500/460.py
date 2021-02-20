from collections import OrderedDict
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.data = {}
        self.freq2keys = {}
        self.key2freq = {}
        self.cap = capacity
        self.min_freq = 0

    def get(self, key, visit=1):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.data:
            return -1
        freq = self.key2freq.get(key, 0) + visit
        self.key2freq[key] = freq
        if freq not in self.freq2keys:
            self.freq2keys[freq] = OrderedDict()
        if key not in self.freq2keys[freq]:
            self.freq2keys[freq][key]=True
        if freq-1 in self.freq2keys:
            if key in self.freq2keys[freq-1]:
                self.freq2keys[freq-1].pop(key)
        if freq-1 == self.min_freq and not self.freq2keys.get(freq-1, None):
            self.min_freq = freq
        if freq == 0:
            self.min_freq = 0
        return self.data[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.cap == 0:
            return
        visit = 1 if key in self.data else 0
        self.data[key] = value
        if len(self.data) > self.cap:
            # print key, value
            # print self.min_freq
            # print self.freq2keys
            # print self.key2freq
            # print self.data
            # print ''
            keys = self.freq2keys.get(self.min_freq, None)
            if keys:
                min_key = keys.iterkeys().next()
                if min_key in keys:
                    keys.pop(min_key)
                if min_key in self.data:
                    self.data.pop(min_key)
                if min_key in self.key2freq:
                    self.key2freq.pop(min_key)
        self.get(key, visit)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)