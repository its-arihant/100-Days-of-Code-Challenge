# Trailing zeros in factorial
def countzeroes(n):
    res=0
    i=5
    while(i<=n):
        res=res+n//i
        i=i*5
    return res

a=int(input("Enter a number:"))
print("The trailing zeroes in factorial of",a,"are:",countzeroes(a)) 

# for finding the trailing zeros we can simply count the number of 2's and 5's
# The number of 5's will be less than the number of 2's
# so we only count number of 5's

# Time complexity=Theta(log(n))