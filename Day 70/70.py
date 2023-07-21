# Leader in an array

class Solution():
    def leader(self,n):
        max=min(n)
        for i in range(len(n)-1,-1,-1):
            if(n[i]>max):
                print(n[i])
            max=n[i]

a=Solution()
a.leader([8,2,3])