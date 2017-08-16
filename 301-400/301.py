class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if self.valid(s):
            return [s]
        q = [s]
        ret = set()
        while True:
            p = set()
            while len(q) > 0:
                ss = q.pop()
                for i in range(len(ss)):
                    if ss[i] == '(' or ss[i] == ')':
                        sss = ss[:i]+ss[i+1:]
                        if self.valid(sss):
                            ret.add(sss)
                        else:
                            p.add(sss)
            if len(ret) > 0:
                break
            q = list(p)
        return list(ret)
        
    def valid(self, s):
        buf = []
        for i in range(len(s)):
            if s[i] != '(' and s[i] != ')':
                continue
            elif s[i] == '(':
                buf.append(s[i])
            elif len(buf) > 0 and buf[-1] == '(':
                buf.pop()
            else:
                return False
        return len(buf)==0
