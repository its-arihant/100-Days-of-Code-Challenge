# 1528 Shuffle String

class Solution:
    def shuffle(self,s,indices):
        a=list(s)
        for i in range(len(a)):
            a[indices[i]]=s[i]
        return "".join(a)

a=Solution()
print(a.shuffle("codeleet",[4,5,6,7,0,2,1,3]))
