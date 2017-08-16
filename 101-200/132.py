class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if size <= 1:
            return 0
        pal = self.palrange(s)
        ret = [0]*size
        for i in range(1, size):
            ret[i] = ret[i-1]+1
            for j in range(i):
                left, right = 2*j+1, 2*i+1
                pleft, pright = pal[(left+right)/2]
                if pleft <= left and right <= pright and left-pleft == pright-right:
                    if j == 0:
                        ret[i] = 0
                        break
                    else:
                        ret[i] = min(ret[i], ret[j-1]+1)
        return ret[-1]
        
    def palrange(self, s):
        arr = ['#']
        for ss in s:
            arr.append(ss)
            arr.append('#')
        size = len(arr)
        p = [1]*size
        ret = []
        right, index = -1, -1
        for i in range(size):
            if i < right:
                p[i] = min(p[2*index-i], right-i)
            l, r = i-p[i], i+p[i]
            while l >= 0 and r < size and arr[l] == arr[r]:
                p[i] += 1
                l -= 1
                r += 1
            if r > right:
                right = r
                index = i
            if l+2 <= r-2:
                ret.append((l+2,r-2))
            else:
                ret.append((-1,-1))
        return ret
