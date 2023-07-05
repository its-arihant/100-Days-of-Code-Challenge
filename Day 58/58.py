# 1748. Sum of Unique Elements

class Solution():
    def sumOfUnique(self, nums):
        c=0
        l=[]
        for i in nums:
            for j in range(len(nums)):
                if i==nums[j]:
                    c=c+1
            if c==1:
                l.append(i)
            c=0
        
        return sum(l)
    

a=Solution()
print(a.sumOfUnique([0,0,0,0]))