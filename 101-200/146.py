from collections import deque
class LRUCache(object):

	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.cap = capacity
		self.freq = {}
		self.data = {}
		self.op = deque([])
		self.total = 0

	def get(self, key):
		"""
		:rtype: int
		"""
		if key not in self.data:
			return -1
		else:
			self.op.append(key)
			self.freq[key] += 1
			return self.data[key]

	def set(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: nothing
		"""
		if key in self.data:
			self.freq[key] += 1
		else:
			self.freq[key] = 1
			self.total += 1
			while self.total > self.cap:
				x = self.op.popleft()
				if self.freq[x] > 1:
					self.freq[x] -= 1
				else:
					del self.freq[x]
					del self.data[x]
					self.total -= 1
		self.data[key] = value
		self.op.append(key)
