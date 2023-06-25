#normal approach
def prime(n):
    if n==1:
        return False
    i=2
    while i*i<=n:
        if(n%i==0):
            return False
        i+=1
    return True

def normal(n):
    for j in range(2,n+1):
        if prime(j):
            print(j,end=" ")

n=int(input("Enter a number:"))
normal(n)
# Time Complexity = O(n*squareroot(n))


# Sieve of Eratostenes

def sieve(n):
    if n<=1:
        return 
    isprime= [True]*(n+1)
    i=2
    while i<=n:
        if isprime[i]:
            print(i,end=" ")
            for j in range(i*i,n+1,i):
                isprime[j]=False
        i+=1

n=int(input("Enter a number:"))
sieve(n)
# Time complexity = O(nlog(log(n)))