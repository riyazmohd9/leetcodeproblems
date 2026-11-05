class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        dp = [-1]*(n+1)
        if dp[n] != -1:
            return dp[n]
        return self.fib(n-1)+self.fib(n-2)
        
        