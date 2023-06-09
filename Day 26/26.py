# 78 Subsets

class Solution:
    def find(self,nums):
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                currSubset = subsets[i]
                subsets.append(currSubset + [num])
        return subsets


a=Solution()
print(a.find([4,3,2,1]))