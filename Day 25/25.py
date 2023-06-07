# 1 Two Sum

class Solution:
    def twosum(self,nums,target):
        a=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    a.extend([i,j])
        return a
a=Solution()
print(a.twosum([3,3],6))
            

        