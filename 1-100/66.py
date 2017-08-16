class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        size = len(digits)
        digits[-1] += 1
        for i in range(1,size+1):
            if digits[-i] == 10:
                digits[-i] = 0
                if i < size:
                    digits[-i-1] += 1
                else:
                    digits.insert(0, 1)
            else:
                break
        return digits
