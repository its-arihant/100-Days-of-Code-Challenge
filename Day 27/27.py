# 1108 Defanging an IP Address

class Solution:
    def ip(self,address):
        return address.replace(".","[.]")

a=Solution()
print(a.ip("255.100.50.0"))