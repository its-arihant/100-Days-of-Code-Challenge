# computing the power

def power(x,n):
    if n==0:
        return 1
    temp=power(x,n//2)
    temp=temp*temp
    if n%2==0:
        return temp
    else:
        return temp*x

x=int(input("Enter the number:"))
n=int(input("Enter the power of number:"))
print(power(x,n))

# T(n)=T(n/2) + theta(1)
# T(n) = O(log(n)) 