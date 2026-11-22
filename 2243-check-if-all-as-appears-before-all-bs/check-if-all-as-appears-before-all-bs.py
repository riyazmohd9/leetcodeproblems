class Solution:
    def checkString(self, s: str) -> bool:
        if "b" in s:
            temp = s.index("b")
            for i in range(temp,len(s)):
                if s[i] == "a":
                    return False
        return True
        