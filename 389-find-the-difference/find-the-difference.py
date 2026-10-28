class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = {}
        
        # Count frequencies in s
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        # Match against t
        for char in t:
            if char not in counts or counts[char] == 0:
                return char
            counts[char] -= 1