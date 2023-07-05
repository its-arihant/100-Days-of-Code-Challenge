# 728. Self Dividing Numbers

class Solution():
    def selfDividingNumbers(self, left, right):
        l=[]
        for i in range(left,right+1):
            if "0" not in str(i):
                d=True
                for j in str(i):
                    if(i%int(j)!=0):
                        d=False
                if d:
                    l.append(i)
        return l
    
a=Solution()
print(a.selfDividingNumbers(1,22))