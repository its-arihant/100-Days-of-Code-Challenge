# 1688. Count of Matches in Tournament

class Solution():
    def numberOfMatches(self, n):
        c=0
        while n>=2:
            if n%2==0:
                m=n/2
                a=n/2
            else:
                m=(n-1)/2
                a=((n-1)/2)+1
            n=a
            c=c+m
        return c

a=Solution()
print(a.numberOfMatches(14))