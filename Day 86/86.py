# 1725. Number Of Rectangles That Can Form The Largest Square

class Solution():
    def countGoodRectangles(self, rectangles):
        l=[]
        for i in rectangles:
            l.append(min(i))
        return l.count(max(l))
    
a=Solution()
print(a.countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]))