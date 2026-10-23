class Solution:
    def reverse(self, x: int) -> int:
        r = str(x)
        if x>0:
            r = r[::-1]
            while r[0] == 0:
                r.remove(r[0])
            if int(r)<2147483647:
                return int(r)
            return 0
        elif x<0:
            r= r[:0:-1]
            if int(r)*-1>=-2147483648:
                return int(r)*-1
            return 0
        return 0
     




        