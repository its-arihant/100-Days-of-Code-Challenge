# 1672 Richest Customer Wealth

class Solution:
    def wealth(self,accounts):
        c=0
        a=[]
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                c+=accounts[i][j]
            a.append(c)
            c=0
        return max(a)
    
a=Solution()
print(a.wealth([[1,5],[7,3],[3,5]]))


