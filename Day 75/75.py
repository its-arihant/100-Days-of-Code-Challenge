# 1780. Check if Number is a Sum of Powers of Three

class Solution():
    def checkPowersOfThree(self, n):
        while n:
            n, rem = divmod(n, 3)
            if rem == 2:
                return False
        return True

a=Solution()
print(a.checkPowersOfThree(12))