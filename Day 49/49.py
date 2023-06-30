# 1281. Subtract the Product and Sum of Digits of an Integer

class solution():
    def diff(self,n):
        p=1
        s=0
        for i in str(n):
            print(i)
            p*=int(i)
            s+=int(i)
        return p-s
            

a=solution()
print(a.diff(77))

            
