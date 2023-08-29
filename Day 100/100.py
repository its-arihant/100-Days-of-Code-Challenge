# 2085. Count Common Words With One Occurrence

class Solution():
    def countWords(self, words1, words2):
        c=0
        for i in words1:
            if words1.count(i)==1 and i in words2 and words2.count(i)==1:
                c+=1
        return c

a=Solution()
print(a.countWords(["leetcode","is","amazing","as","is"],["amazing","leetcode","is"]))