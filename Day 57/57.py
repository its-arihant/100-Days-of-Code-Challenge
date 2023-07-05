# 1979. Find Greatest Common Divisor of Array

class Solution():
    def findGCD(self, nums):
        l=[]
        a=min(nums)
        b=max(nums)
        for i in range(1,a+1):
            if (a%i==0 and b%i==0):
                l.append(i)
        return max(l)
    
a=Solution()
print(a.findGCD([2,5,6,9,10]))
