# 136. Single Number

class Solution():
    def singleNumber(self, nums):
        for i in nums:
            if nums.count(i)==1:
                return i

a=Solution()
print(a.singleNumber([2,2,1]))
