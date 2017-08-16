class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        size = len(ratings)
        if size == 0:
            return 0
        ret = [1]*size
        for i in range(1,size):
            if ratings[i] == ratings[i-1]:
                ret[i] = 1
            elif ratings[i] > ratings[i-1]:
                ret[i] = ret[i-1]+1
        for i in range(-2, -size-1, -1):
            if ratings[i] > ratings[i+1] and ret[i] < ret[i+1]+1:
                ret[i] = ret[i+1]+1
        return sum(ret)
