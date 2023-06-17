#sum of first n natural numbers
def sumofn(n):
    return ((n*(n+1))/2)

n=int(input("Enter the value of n to which you want sum:"))
print("Sum of first",n,"natural numbers is:",sumofn(n))
#we get float value as we used single division operator
#and if we use double division operator then it will give int value as it becomes floor operator
#Time complexity = O(1) as it is not dependent on n

#count digits
def count(n):
    res=0
    while n>0:
        n=n//10
        res+=1
    print("count:",res)

n=int(input("Enter a number:"))
count(n)
#Time complexity = theta(countdigits) as loop runs for the number of digis present in the number
        
