class Solution(object):
	def findLadders(self, beginWord, endWord, wordlist):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordlist: Set[str]
		:rtype: List[List[int]]
		"""
		path1, path2 = [[beginWord]], [[endWord]]
		visit1, visit2 = set(), set()
		ret = []
		k = len(beginWord)
		while len(path1) != 0 and len(path2) != 0:
			path1 = self.expand(path1, wordlist, visit1, k)
			self.merge(path1, path2, ret)
			if len(ret) > 0:
				return ret
			path2 = self.expand(path2, wordlist, visit2, k)
			self.merge(path1, path2, ret)
			if len(ret) > 0:
				return ret
		return []
		
	def expand(self, path, wordlist, visit, k):
		ret, vis = [], set()
		for p in path:
			word = p[-1]
			for i in range(k):
				for j in 'abcdefghijklmnopqrstuvwxyz':
					w = word[:i]+j+word[i+1:]
					if w in wordlist and w not in visit:
						ret.append(p+[w])
						vis.add(w)
		for w in vis:
			visit.add(w)
		return ret
		
	def merge(self, path1, path2, ret):
		for p1 in path1:
			for p2 in path2:
				if p1[-1] == p2[-1]:
					tmp = p2[:-1]
					tmp.reverse()
					ret.append(p1 + tmp)
