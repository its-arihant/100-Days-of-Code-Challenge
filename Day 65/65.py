# 2544. Alternating Digit S

class Solution():
    def alternateDigitSum(self, n):
        c=0
        a=str(n)
        for i in range(0,len(a)):
            if i%2==0:
                c=c+int(a[i])
            else:
                c=c-int(a[i])
        return c

a=Solution()
print(a.alternateDigitSum(521))