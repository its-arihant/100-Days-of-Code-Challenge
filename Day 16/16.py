# 1773 Count Items Matching a Rule

class Solution:
    def match(self,items,ruleKey,ruleValue):
        c=0
        for i in items:
            if ruleKey == "type" and ruleValue ==i[0]:
                c+=1
            elif ruleKey == "color" and ruleValue == i[1]:
                c+=1
            elif ruleKey == "name" and ruleValue == i[2]:
                c+=1
        return c

a=Solution()
print(a.match([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))
