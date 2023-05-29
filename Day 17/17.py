# 2367 Number of Arithmetic Triplets

class Solution:
    def triplets(self,nums,diff):
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if ((i < j < k) and (nums[j] - nums[i] == diff)  and (nums[k] - nums[j] == diff)):
                        c+=1

        return c

a=Solution()
print(a.triplets([0,1,4,6,7,10],3))
