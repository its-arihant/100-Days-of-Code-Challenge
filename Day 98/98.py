# 977. Squares of a Sorted Array

class Solution():
    def sortedSquares(self, nums):
        a=[]
        for i in nums:
            a.append(i**2)
        return sorted(a)

a=Solution()
print(a.sortedSquares([-4,-1,0,3,10]))
