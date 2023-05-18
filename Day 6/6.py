# 1431 Kids With the Greatest Number of Candies

class Solution:
    def candy(self,candies,extraCandies):
        a=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max(candies):
                a.append(True)
            else:
                a.append(False)
        return a
    
b=Solution()
print(b.candy([4,2,1,1,2],1))

