class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0, len(numbers)-1
        while j>i:
            if numbers[i]+numbers[j] == target:
                break
            elif numbers[i]+numbers[j] > target:
                j-=1;
            else:
                i+=1;
        return [i+1, j+1]
