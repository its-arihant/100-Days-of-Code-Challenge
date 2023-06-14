# 1844 Replace All Digits with Characters

class Solution:
    def digits(self,s):
        a = list(s)
        for i in range(1, len(a), 2):
            a[i] = chr(ord(a[i - 1]) + int(a[i]))
        return ''.join(a)
    
a=Solution()
print(a.digits("a1c1e1"))

