# 258. Add Digits

class solution():
   def add(self,num):
      while num > 9:
         sum = 0
         while num:
            sum += num%10
            num = num//10
         num = sum
      return num
            

a=solution()
print(a.add(77))