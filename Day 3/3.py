# 2011 Final Value of Variable After Performing Operations

class Sol:
    def ans(self,operations):
        X=0
        for i in range(len(operations)):
            if  operations[i]=='++X' or operations[i]=='X++' :
                X=X+1
            else:
                X=X-1
        return X

b=Sol()
print(b.ans(['X++','X--'])) 