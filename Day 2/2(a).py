# 1920 Build Array from Permutation
class Sol:
    def build(self,nums):
        ans=[]
        for i in range(0,len(nums)):
            ans.append(nums[nums[i]])
        return ans

a=Sol()
print(a.build([0,2,1,5,3,4]))