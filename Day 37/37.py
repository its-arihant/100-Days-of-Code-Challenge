#HCF or GCD of 2 numbers
def hcf(a,b):
    if(b==0):
        return a
    else:
        return(hcf(a,a%b))
    
#LCM of 2 numbers
# LCM * GCD = Product of 2 numbers
# LCM = Product of 2 numbers/GCD
def lcm(a,b):
    return int(((a*b)/hcf(a,b)))


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("The HCF of two numbers",a,"and",b,"is:",hcf(a,b))
print("The LCM of two numbers",a,"and",b,"is:",lcm(a,b))

#Time comlexity = O(log(min(a,b)))
