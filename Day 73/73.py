# 2744. Find Maximum Number of String Pairs

class Solution():
    def maximumNumberOfStringPairs(self, words):
        c=0
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                if words[j][::-1]==words[i]:
                    c=c+1
        return c

a=Solution()
print(a.maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))