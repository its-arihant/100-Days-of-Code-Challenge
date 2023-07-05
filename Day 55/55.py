# 1812. Determine Color of a Chessboard Square

class Solution():
    def squareIsWhite(self, coordinates):
       if coordinates[0] in 'aceg':
            return int(coordinates[1])%2 == 0
       if coordinates[0] in 'bdfh':
            return int(coordinates[1])%2 == 1


a=Solution()
print(a.squareIsWhite("a1"))