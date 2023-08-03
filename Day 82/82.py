# 2221. Find Triangular Sum of an Array

class Solution():
    def triangularSum(self, nums):
        if len(nums)==1:
            return nums[0]
        j = 0
        n = len(nums)
        while(j < n-1):
            for i in range(n-j-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            j += 1
        return nums[0]

a=Solution()
print(a.triangularSum([1,2,3,4,5]))