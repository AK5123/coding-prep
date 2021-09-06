# https://leetcode.com/problems/perfect-squares/
import math
class Solution:
    def numSquares(self, n):
        dp = [0,1,2,3]
        
        if n<=3:
            return dp[n]
        
        for i in range(4,n+1):
            dp.append(i);
            
            for j in range(1,math.ceil(math.sqrt(i))+1):
                if j*j <= i:
                    dp[i] = min(dp[i],dp[i-(j**2)]+1)
        return dp[n]        