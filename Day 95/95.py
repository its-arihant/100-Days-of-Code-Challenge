# 1207. Unique Number of Occurrences

class Solution():
    def uniqueOccurrences(self, arr):
        nums = []
        occurences = []
        for num in arr:
            if num not in nums:
                occurence = arr.count(num)
                if occurence not in occurences:
                    occurences += [occurence]
                    nums += [num]
                else:
                    return False
        return True

a=Solution()
print(a.uniqueOccurrences([1,2,2,1,1,3]))