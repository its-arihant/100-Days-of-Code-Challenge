# 1389 Create Target Array in the Given Order

class Solution:
    def new(self,nums,index):
        a=[]
        for i in range(len(nums)):
            a.insert(index[i],nums[i])
        return a
    
a=Solution()
print(a.new([0,1,2,3,4],[0,1,2,2,1]))

