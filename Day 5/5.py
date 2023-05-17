# 2574 Left and Right Sum Differences

class Solution:
    def sum(self,nums):
       answer=[]
       left=0
       right=sum(nums)
       for i in nums:
           right-=i
           answer.append(abs(left-right))
           left+=i
       return answer
    

a=Solution()
print(a.sum([1]))

            


        
