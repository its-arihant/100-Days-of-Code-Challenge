# 2185. Counting Words With a Given Prefix

class Solution:
    def prefixCount(self, words, pref):
        c=0
        a=len(pref)
        for i in words:
            if i[0:a]==pref:
                c+=1
        return c

a=Solution()
print(a.prefixCount(["pay","attention","practice","attend"],"at"))