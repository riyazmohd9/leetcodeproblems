class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(1,len(s)+1,1):
            total += (123 - ord(s[i-1]))*i
        return total
        