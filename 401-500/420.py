class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        lower = 0 if any('a'<=x<='z' for x in s) else 1
        upper = 0 if any('A'<=x<='Z' for x in s) else 1
        digit = 0 if any('0'<=x<='9' for x in s) else 1
        
        last, count, repl, num = '', 0, 0, [0]*3
        for i in range(len(s)):
            if last == s[i]:
                count += 1
            if last != s[i] or i == len(s)-1:
                if count > 2:
                    repl += count/3
                    num[count%3] += 1
                last = s[i]
                count = 1
                
        if len(s) < 6:
            return max(6-len(s), lower+upper+digit)
        elif len(s) <= 20:
            return max(repl, lower+upper+digit)
        else:
            delete = len(s)-20
            repl -= min(num[0], delete)
            repl -= min(max(delete-num[0], 0), num[1]*2)/2
            repl -= max(delete-num[0]-num[1]*2, 0)/3
            return delete + max(repl, lower+upper+digit)
        
