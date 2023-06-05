# 1913 Maximum Product Difference Between Two Pairs

class Solution:
    def product(self,nums):
        nums.sort()
        return (nums[-1]*nums[-2])-(nums[0]*nums[1])

a=Solution()
print(a.product([4,2,5,9,7,4,8]))
