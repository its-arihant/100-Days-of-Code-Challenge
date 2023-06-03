# 2006 Count Number of Pairs With Absolute Difference K

class Solution:
    def count(self,nums,k):
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and abs(nums[i] - nums[j])==k:
                    c+=1
        return c
a=Solution()
print(a.count([1,2,2,1],1))