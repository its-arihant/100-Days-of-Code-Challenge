# 1929 Concatenation of Array

class Solution(object):
    def getConcatenation(self,nums):
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[i])

        if len(ans)==len(nums):
            for i in range(len(nums)):
                ans.append(nums[i])
        return ans

a=Solution()
print(a.getConcatenation([1,1,6,2]))