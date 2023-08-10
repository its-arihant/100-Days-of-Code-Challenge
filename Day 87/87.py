# 2215. Find the Difference of Two Arrays

class Solution():
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]

a=Solution()
print(a.findDifference([1,2,3],[2,4,6]))