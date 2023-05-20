# 1480 Running Sum of 1d Array

class Solution:
    def running(self,nums):
        c=0
        a=[]
        for i in range(len(nums)):
            c+=nums[i]
            a.append(c)
        return a
    
a=Solution()
print(a.running([1,2,3,4]))
            
