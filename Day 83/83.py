# 2000. Reverse Prefix of Word

class Solution():
    def reversePrefix(self, word, ch):
        if ch in word:
            i=word.index(ch)
            w=word[:i+1]
            return w[::-1]+word[i+1:]
        else:
            return word

a=Solution()
print(a.reversePrefix("abcdefd","d"))