# 9 Palindrome Number

class Solution:
    def find(self,x):
        a=list(str(x))
        if a==a[::-1]:
            return True
        else:
            return False
        
a=Solution()
print(a.find(121))