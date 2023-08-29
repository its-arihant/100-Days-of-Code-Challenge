# 2586. Count the Number of Vowel Strings in Range

class Solution():
     def vowelStrings(self, words, left, right):
        a="aeiou"
        c=0
        for i in range(0,len(words)):
            if left<=i<=right and words[i][0] in a and words[i][-1] in a:
                c=c+1
        return c

a=Solution()
print(a.vowelStrings(["are","amy","u"],0,2))