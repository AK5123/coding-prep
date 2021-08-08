# https://leetcode.com/problems/jump-game-ii/
class Solution:
    def jump(self, n):
        dp = [0]*(len(n))
        cur = 1
        for i in range(len(n)):
            j = i + n[i]
            if j >= cur:
                k = cur
                while k<len(n) and k <= j:
                    dp[k] = dp[i] + 1
                    k += 1
                cur = k
                if cur == len(n):
                    return dp[-1]
        return dp[-1]            
                    