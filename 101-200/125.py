import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = "".join(re.findall("[a-zA-Z0-9]*", s)).lower()
        return check == check[::-1]
