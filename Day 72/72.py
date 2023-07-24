# 2103. Rings and Rods

class Solution():
    def countPoints(self, rings):
        c=0
        for i in range(0,10):
            if 'R'+str(i) in rings and 'G'+str(i) in rings and 'B'+str(i) in rings:
                c=c+1
        return c

a=Solution()
print(a.countPoints("B0B6G0R6R0R6G9"))
