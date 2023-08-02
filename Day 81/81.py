# 2442. Count Number of Distinct Integers After Reverse Operations

class Solution():
     def countDistinctIntegers(self, nums):
        new=[]
        for i in nums:
            new.append(int(str(i)[::-1]))  
        nums.extend(new)                     
        return len(set(nums)) 

a=Solution()
print(a.countDistinctIntegers([1,13,10,12,31]))

