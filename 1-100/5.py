class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        arr = ['#']
        for ss in s:
            arr.append(ss)
            arr.append('#')
        size = len(arr)
        p = [1]*size
        right, index = -1, -1
        center, radius = -1, -1
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
            if radius < p[i]:
                center = i
                radius = p[i]
        ret = ''
        for i in range(center-radius+1, center+radius):
            if arr[i] != '#':
                ret += arr[i]
        return ret
            
