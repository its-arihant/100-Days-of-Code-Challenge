# 2529. Maximum Count of Positive Integer and Negative Integer

class Solution:
     def maximumCount(self, nums):
        a=0
        b=0
        for i in nums:
            if i>0:
                a+=1
            elif i<0:
                b+=1
        return max(a,b)
     
a=Solution()
print(a.maximumCount([-2,-1,-1,1,2,3]))
