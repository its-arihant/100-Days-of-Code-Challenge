# 1470 Shuffle the Array
class Sol:
    def build(self,nums,n):
        a=[]
        b=[]
        c=[]
        for i in range(0,n):
            a.append(nums[i])
        for j in range(n,(len(nums))):
            b.append(nums[j])
        for k in range(0,n):
            c.append(a[k])
            c.append(b[k])
        return c

b=Sol()
print(b.build([1,2,3,4,5,6],3))
