# 1295. Find Numbers with Even Number of Digits

class Solution():
    def findNumbers(self, nums):
        c=0
        for i in nums:
            if len(str(i))%2==0:
                c+=1
        return c

a=Solution()
print(a.findNumbers([12,345,2,6,7896]))