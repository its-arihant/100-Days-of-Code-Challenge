# 1588 Sum of All Odd Length Subarrays

class Solution:
    def odd(self,arr):
        s=0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                s+=sum(arr[i:j+1])
        return s
    
a=Solution()
print(a.odd([1,4,2,5,3]))
