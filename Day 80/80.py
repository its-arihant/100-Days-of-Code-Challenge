# 1464 Maximum Product of Two Elements in an Array

class Solution():
    def maxProduct(self, nums):
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)

a=Solution()
print(a.maxProduct([3,4,5,2]))
