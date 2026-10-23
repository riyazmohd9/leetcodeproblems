class Solution:
    def sumAndMultiply(self, n: int) -> int:
        r = str(n)
        sum = 0
        s = ""
        for i in r:
            if i != "0":
                s += i
                sum += int(i)
        return int(s)*sum if s else 0
        