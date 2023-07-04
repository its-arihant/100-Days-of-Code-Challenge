# 2520. Count the Digits That Divide a Number

class Solution():
    def count(self,num):
        c=0
        for i in str(num):
            if (num%(int(i))==0):
                c+=1
        return c
    
a=Solution()
print(a.count(121))
