# 2656 Maximum Sum With Exactly K Elements 

class Solution:
    def maximum(self,nums,k):
        s=0
        nums.sort()
        for i in range(k):
            s+=nums[-1]
            nums[-1]+=1
        return s
a=Solution()
print(a.maximum([1,2,3,4,5],3))
