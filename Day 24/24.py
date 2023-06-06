# 2418 Sort the People

class Solution:
    def people(self,names,heights):
        d={}
        for i in range(len(names)):
            d[heights[i]]=names[i]
        heights.sort(reverse=True)
        for i in range(len(heights)):
            names[i]=d[heights[i]]
        return names
       
a=Solution()
print(a.people(["Mary","John","Emma"],[180,165,170]))