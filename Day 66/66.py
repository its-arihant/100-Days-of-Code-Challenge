# 1832. Check if the Sentence Is Pangram

class Solution():
    def checkIfPangram(self, sentence):
        if len(set(sentence))==26:
            return True
        else:
            return False
        
a=Solution()
print(a.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
