# 905. Sort Array By Parity

class Solution():
    def sortArrayByParity(self, nums):
        l=[]
        for i in nums:
            if i%2==0:
                l.insert(0,i)
            else:
                l.append(i)
        return l

a=Solution()
print(a.sortArrayByParity([3,1,2,4]))