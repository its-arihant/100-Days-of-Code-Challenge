# 1941 Check if All Characters Have Equal Number of Occurrences

class Solution():
    def areOccurrencesEqual(self, s):
        m=s.count(s[0])
        for i in s:
            if s.count(i)!=m: return False
        return True
    

a=Solution()
print(a.areOccurrencesEqual("abacbc"))