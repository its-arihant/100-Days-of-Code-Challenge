# 125. Valid Palindrome

class Solution():
    def isPalindrome(self, s):
        l=[]
        for i in s:
            for j in i:
                if j.isalpha()==True or j.isdigit()==True:
                    l.append(j.lower())
        a="".join(l)
        return (a[::-1]==a)


a=Solution()
print(a.isPalindrome("0P"))