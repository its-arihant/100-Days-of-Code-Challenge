# 2176 Count Equal and Divisible Pairs in an Array

class Solution():
    def countPairs(self, nums, k):
        c=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i<j<len(nums) and nums[i]==nums[j] and (i*j)%k==0:
                    c=c+1
        return c

a=Solution()
print(a.countPairs([3,1,2,2,2,1,3],2))
