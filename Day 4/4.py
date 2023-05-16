# 1512 Number of Good Pairs

class Solution:
    def pair(self,nums):
        count=0
        for i in range(len(nums)):
             for j in range(len(nums)):
                if (nums[i]==nums[j]) and (i<j):
                    count+=1
        return count

a=Solution()
print(a.pair([1,1,1,1]))



