# 2315 Count Asterisks

class Solution:
    def count(self,s):
        a=s.split("|")
        c=0
        for i in range(0,len(a),2):
            for j in a[i]:
                if j=="*":
                   c+=1
        return c
a=Solution()
print(a.count("l|*e*et|c**o|*de|"))