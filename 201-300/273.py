class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        self.m = {'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen','19':'Nineteen','20':'Twenty','30':'Thirty','40':'Forty','50':'Fifty','60':'Sixty','70':'Seventy','80':'Eighty','90':'Ninety'}
        mm = ['Thousand', 'Million', 'Billion']
        ret = ''
        c = 0
        while num > 0:
            n = num % 1000
            num = int(num / 1000)
            s = self.encode(str(n))
            if s != '':
                ret = s if c == 0 else s + ' ' + mm[c-1] + ' ' + ret
            c += 1
        return ret.strip()
        
    def encode(self, n):
        ret = ''
        if len(n) > 2 and n[-3] != '0':
            ret += self.m[n[-3]] + ' Hundred '
        if len(n) > 1 and n[-2] != '0':
            if n[-2] == '1' or n[-1] == '0':
                ret += self.m[n[-2:]]
                return ret
            else:
                ret += (self.m[n[-2]+'0'] + ' ')
        if len(n) > 0 and n[-1] != '0':
            ret += self.m[n[-1]]
        return ret.strip()
