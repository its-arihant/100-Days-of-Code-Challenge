# 1684. Count the Number of Consistent Strings

class find:
    def consistent(self,allowed,words):
        count =0
        for i in words:
            for j in i:
                if j not in allowed:
                    count+=1
                    break
        return len(words)-count    
    
a=find()
print(a.consistent("ab",["ad","bd","aaab","baa","badab"]))


