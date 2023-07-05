# 2180. Count Integers With Even Digit Sum

class Solution():
    def countEven(self, num):
        s=0
        c=0
        for i in range(1,num+1):
            if(len(str(i))>1):
                for j in str(i):
                    s=s+int(j)
                if (s%2==0):
                    c=c+1
                s=0
            else:
                if(i%2==0):
                    c=c+1
        return c

a=Solution()
print(a.countEven(30))

