# 2678. Number of Senior Citizens

class Solution():
    def countSeniors(self, details):
        c=0
        for i in details:
            if int(i[11:13])>60:
                c+=1
        return c

a=Solution()
print(a.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))