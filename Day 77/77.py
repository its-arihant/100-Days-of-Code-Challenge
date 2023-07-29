# 1822. Sign of the Product of an Array

class Solution():
    def arraySign(self, nums):
        a=1
        for i in nums:
            a=a*i
        if a>0:
            return 1
        elif a<0:
            return -1
        else:
            return 0

b=Solution()
print(b.arraySign([-1,-2,-3,-4,3,2,1]))
