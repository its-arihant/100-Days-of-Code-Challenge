# 1051. Height Checker

class Solution():
    def heightChecker(self, heights):
        c=0
        l=sorted(heights)
        for i in range(0,len(heights)):
            if heights[i] != l[i]:
                c+=1
        return c

a=Solution()
print(a.heightChecker([1,1,4,2,1,3]))