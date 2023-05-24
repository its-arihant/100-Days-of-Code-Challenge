# 1313 Decompress Run-Length Encoded List

class Solution:
    def find(self,nums):
        a=[]
        for i in range(0,len(nums),2):
            freq=nums[i]
            val=nums[i+1]
            a+=([val]*freq)
        return a

a=Solution()
print(a.find([1,2,3,4]))



