class Solution:
    def countDigits(self, num: int) -> int:
        p=num
        count=0
        while num>0:
            r=num%10
            if p%r==0:
                count+=1
            num=num//10
        return count        