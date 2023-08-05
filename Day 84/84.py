# 2778 Sum of Squares of Special Elements

class Solution():
    def sumOfSquares(self, nums):
        a=0
        for i in range(1,len(nums)+1):
            if len(nums)%i==0:
                a=a+(nums[i-1]**2)
        return a

a=Solution()
print(a.sumOfSquares([1,2,3,4]))
