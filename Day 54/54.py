# 2427 Number of Common Factors

class Solution():
    def commonFactors(self, a, b):
        c=0
        for i in range(1,min(a,b)+1):
            if(a%i==0 and b%i==0):
                c+=1
        return c

a=Solution()
print(a.commonFactors(12,6))