# Moving hypens to the beginning of the string

def hypen(n):
    c=0
    m=[]
    l=list(n)
    print(l)
    for i in l:
        if i=="-":
            c=c+1
        elif i!="-":
            m.append(i)

    for i in range(1,c+1):
        m.insert(0,"-")
    
    return "".join(m)

a=input("Enter a string:")
print(hypen(a))  