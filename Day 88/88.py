# 2733. Neither Minimum nor Maximum

class Solution():
    def findNonMinOrMax(self, nums):
        nums.sort()
        if len(nums)<3:
            return -1
        else:
            return nums[1]

a=Solution()
print(a.findNonMinOrMax([3,2,1,4]))