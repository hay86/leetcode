class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        while i < len(str):
            if '0' <= str[i] <= '9':
                break
            elif str[i] == '+' or str[i] == '-':
                if i+1 < len(str) and '0' <= str[i+1] <= '9':
                    break
                else:
                    return 0
            elif str[i] != ' ':
                return 0
            i += 1
        str = str[i:i+12]
        if str == '':
            return 0
        i = 1
        while i < len(str):
            if str[i] < '0' or str[i] > '9':
                break
            i += 1
        ret = int(str[:i])
        if ret > 2147483647:
            ret = 2147483647
        if ret < -2147483648:
            ret = -2147483648
        return ret
            
