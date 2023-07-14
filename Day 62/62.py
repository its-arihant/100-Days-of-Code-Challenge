# 1323 Maximum 69 Number

class Solution():
     def maximum69Number (self, num):
        a=list(str(num))
        print(a)
        for i in range(len(a)):
            if (a[i]=='6'):
                a[i]='9'
                break
        return int(''.join(a))
    
a=Solution()
print(a.maximum69Number(9669))
        