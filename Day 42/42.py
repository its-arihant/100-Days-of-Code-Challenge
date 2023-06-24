# Prime factorization
def isprime(n):
    if (n==1):
        return False    
    i=2
    while(i*i<=n):
        if (n%i==0):
            return False
        i+=1
    return True

def primefactors(n):
    for i in range(2,n+1):
        if isprime(i):
            #print(i)
            a=i
            while n%a==0:
                print(i)
                a=a*i
 

n=int(input("Enter a number:"))
primefactors(n) 