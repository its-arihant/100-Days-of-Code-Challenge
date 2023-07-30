# 1732. Find the Highest Altitude

class Solution():
    def largestAltitude(self, gain):
        a=0
        m=0
        for i in gain:
            a=a+i
            m=max(a,m)
        return m

a=Solution()
print(a.largestAltitude([-5,1,5,0,-7]))