# 2553. Separate the Digits in an Array

class Solution():
    def separateDigits(self, nums):
        l=[]
        for i in nums:
            if len(str(i))>1:
                for j in str(i):
                    l.append(int(j))
            else:
                l.append(i)
        return l

a=Solution()
print(a.separateDigits([13,25,83,77]))