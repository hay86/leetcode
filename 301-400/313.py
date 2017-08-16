import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ret = [1]
        q = []
        for p in primes:
            heapq.heappush(q, (p,p,0))
        for j in range(n-1):
            v = q[0][0]
            ret.append(v)
            while len(q) > 0 and q[0][0] == v:
                a,b,c = heapq.heappop(q)
                c += 1
                heapq.heappush(q, (b*ret[c],b,c))
        return ret[-1]
