# 1816 Truncate Sentence

class Solution:
    def sentence(self,s,k):
        b=[]
        a=s.split()
        for i in range(len(a)):
            b.append(a[i])
            if i==(k-1):
                break
        return " ".join(b)

a=Solution()
print(a.sentence("Hello how are you Contestant",4))