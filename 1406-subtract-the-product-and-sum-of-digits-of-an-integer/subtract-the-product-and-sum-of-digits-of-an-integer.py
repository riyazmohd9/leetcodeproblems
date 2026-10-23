class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro=1
        s=0
        while n>0:
            
            d=n%10
            pro=pro*d
            s+=d
            n=n//10
        return pro-s   