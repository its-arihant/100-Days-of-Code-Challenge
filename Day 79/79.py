# 1103. Distribute Candies to People

class Solution():
    def distributeCandies(self, candies, num_people):
        c=1
        index=0
        r=[0]*num_people
        while candies>0:
            r[index]+=min(c,candies)
            candies-=c
            index=(index+1)%num_people
            c+=1
        return r
        

a=Solution()
print(a.distributeCandies(7,4))