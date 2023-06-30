# 2413. Smallest Even Multiple

class solution():
    def multiple(self,n):
        if n%2==0:
            return n
        else:
            return 2*n
            

a=solution()
print(a.multiple(77))

            
