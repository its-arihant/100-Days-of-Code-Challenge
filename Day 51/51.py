# 1342. Number of Steps to Reduce a Number to Zero

class Solution():
    def reduce(self,num):
        c=0
        while(num!=0):
            if(num%2==0):
                num=num/2
            else:
                num=num-1
            c=c+1
        return c
    
a=Solution()
print(a.reduce(14))