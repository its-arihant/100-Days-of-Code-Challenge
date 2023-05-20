# 2114 Maximum Number of Words Found in Sentences

class Solution:
    def find(self,sentences):
        b=[]
        for i in sentences:
            a=i.split()
            b.append(len(a))
        return max(b)

a=Solution()
print(a.find(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))

