# 153. Find Minimum in Rotated Sorted Array

class Solution():
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

a=Solution()
print(a.findMin([3,4,5,1,2]))