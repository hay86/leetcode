# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a = rand7()
            b = rand7()
            x = (a-1)*7 + b-1 # 0-48
            if x < 40:
                return x//4 + 1
            a = x-39
            b = rand7()
            x = (a-1)*7 + b-1 # 0-62
            if x < 60:
                return x//6 + 1
            a = x - 59
            b = rand7()
            x = (a-1)*7 + b-1 # 0-20
            if x < 20:
                return x//2 + 1
            
