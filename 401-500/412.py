class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for i in range(1,n+1):
            a, b = i%3, i%5
            if a==0 and b==0:
                ret.append('FizzBuzz')
            elif a==0:
                ret.append('Fizz')
            elif b==0:
                ret.append('Buzz')
            else:
                ret.append(str(i))
        return ret
                
