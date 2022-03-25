import ipaddress

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        try:
            if '::' in queryIP:
                return 'Neither'
            ip = ipaddress.ip_address(queryIP)
            return 'IPv%s' % ip.version
        except Exception as e:
            return 'Neither'
