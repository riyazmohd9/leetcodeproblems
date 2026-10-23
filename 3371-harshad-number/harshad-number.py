class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        r =x
        s = 0
        while x>0:
            s += x%10
            x = x//10
        if r%s != 0:
            return -1
        return s
            
        