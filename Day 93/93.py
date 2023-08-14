# 1450. Number of Students Doing Homework at a Given Time

class Solution():
    def busyStudent(self, startTime, endTime, queryTime):
        c=0
        for i in range(len(startTime)):
            if startTime[i]>=queryTime and endTime[i]<=queryTime:
                c+=1
            elif startTime[i]<=queryTime and endTime[i]>=queryTime:
                c+=1
        return c

a=Solution()
print(a.busyStudent([1,2,3],[3,2,7],4))