#Palindrome number
def num(n):
    rev=0
    temp=n
    while temp>0:
        id = temp%10
        rev=rev*10+id
        temp=temp//10
    if(rev==n):
        print("its palindrome")
    else:
        print("not plaindrome")
    
n=int(input("Enter a number:"))
num(n) 
# time complexity = theta(number of digits of a number)

#Recursive functions
#1. factorial of a number
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

a=int(input("Enter a number:"))
print("The factorial of",a,"is:",fact(a))
#recurrence relation = T(n-1) + theta(1) 
#time complexity = O(n)


