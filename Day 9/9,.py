# 1365 How Many Numbers Are Smaller Than the Current Number

class Solution:
    def small(self,nums):
        a=[]
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] != nums[j] and nums[i] > nums[j]:
                    c+=1
            a.append(c)
            c=0
        return a

a=Solution()
print(a.small([8,1,2,2,3]))

                   

