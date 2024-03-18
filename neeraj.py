#Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr):
        d = {}
        for n in arr:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        result = len(d.values())
        a = len(set(d.values()))
        return result == a

    
