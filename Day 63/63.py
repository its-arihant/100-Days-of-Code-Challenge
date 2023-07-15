# 1304. Find N Unique Integers Sum up to Zero

class Solution():
    def sumZero(self, n):
         return [i*2-n+1 for i in range(0,n)]
a=Solution()
print(a.sumZero(1))