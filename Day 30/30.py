# 1678 Goal Parser Interpretation

class Solution:
    def interpret(self,command):
        a=""
        for i in range(len(command)):
            if command[i]=="G":
                a+="G"
            elif command[i]=="(" and command[i+1]==")":
                a+="o"
            elif command[i]=="(" and command[i+1]=="a"and command[i+2]=="l"and command[i+3]==")":
                a+="al"
        return a
a=Solution()
print(a.interpret("G()(al)"))
