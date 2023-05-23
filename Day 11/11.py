# 1720 Decode XORed Array

class Solution:
    def find(self,encoded,first):
        a=[first]
        for i in range(0,len(encoded)):
            b = encoded[i] ^ a[i]
            a.append(b)
        return a
    
a=Solution()
print(a.find([1,2,3],1))