# 2651. Calculate Delayed Arrival Time

class Solution():
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        s=arrivalTime+delayedTime
        if(s==24):
            return 0
        elif(s>23):
            return s-24
        else:
            return s

a=Solution()
print(a.findDelayedArrivalTime(13,11))