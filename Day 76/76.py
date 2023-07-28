# 2769. Find the Maximum Achievable Number

class Solution():
     def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        return num+(t*2)

a=Solution()
print(a.theMaximumAchievableX(4,1))