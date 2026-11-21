class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            temp = s.count(i)
            if i not in t:
                return False
            elif t.count(i)!= temp:
                return False
        for i in t:
            temp = t.count(i)
            if i not in s:
                return False
            elif s.count(i)!= temp:
                return False
        return True
        