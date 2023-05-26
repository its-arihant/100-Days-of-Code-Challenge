#2652 Sum Multiples

class Solution:
    def multiples(self,n):
        sum=0
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                sum+=i
        return sum
    
a=Solution()
print(a.multiples(10))
