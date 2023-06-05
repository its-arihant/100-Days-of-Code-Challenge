# 804 Unique Morse Code Words

class Solution:
    def unique(self,words):
        b=[]
        e=[]
        l=[]
        c=0
        d={ "a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        for i in words:
            a=list(i)
            for j in a:
                b.append(d[j])
            e.append("".join(b))
            b=[]
        for k in e:
            if k not in l:
                l.append(k)
        return len(l)
a=Solution()
print(a.unique(["gin","zen","gig","msg"]))



