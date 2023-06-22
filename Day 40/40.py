# Divisors of a number
def printdivisor(n):
    i=1
    while(i*i<n):
        if(n%i==0):
            print(i)
        i+=1
    while(i>=1):
        if(n%i==0):
            print(n/i)
        i-=1

n=int(input("Enter a number:"))
print(printdivisor(n))
    
# Time complexity=theta(square root(n))
