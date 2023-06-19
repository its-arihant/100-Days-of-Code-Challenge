# Mathematical problems
# 1. Prime number
# first approach
def prime(n):
    if (n==1):
        return False
    for i in range(2,n):
        if (n%i==0):
            return False
    return True

n=int(input("Enter a number:"))
print(prime(n))
# Time complexity = O(n) 

# 2nd approach(more efficient than previous one)
def prime(n):
    if (n==1):
        return False
    
    i=2
    while(i*i<n):
        if (n%i==0):
            return False
        i+=1
    return True

n=int(input("Enter a number:"))
print(prime(n))
# Time complexity = O(square root(n))
