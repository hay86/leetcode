import math
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        n = minutesToTest/minutesToDie + 1
        # n^x >= buckets
        return int(math.ceil(math.log(buckets, n)))