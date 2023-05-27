# 2535 Difference Between Element Sum and Digit Sum of an Array
 
class Solution:
    def digits(self,nums):
        a=0
        b=0
        for i in nums:
            a+=i
            c=list(str(i))
            for j in range(len(c)):
                    b+=int(c[j])
        return abs(a-b)
        
a=Solution()
print(a.digits([1,15,6,3]))

