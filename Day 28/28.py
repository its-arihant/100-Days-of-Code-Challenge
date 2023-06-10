# 771 Jewels and Stones

class Solution:
    def check(self,jewels,stones):
        c=0
        for i in jewels:
            for j in stones:
                if i==j:
                    c+=1
        return c
    
a=Solution()
print(a.check("aA","aAAbbbb"))