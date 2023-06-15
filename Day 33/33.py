# 66 Plus One

class Solution:
    def plus(self,digits):
        a=""
        b=[]
        for i in digits:
            a+=str(i)
        c=str(int(a)+1)
        for j in c:
            b.append(int(j))
        return(b)

a=Solution()
print(a.plus([9,9,9]))
