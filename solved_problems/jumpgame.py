# https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, n):
        res = set()
        i = len(n)-1
        if len(n) == 1:
            return True
        res.add(i)
        i-=1
        l = len(n)-1
        while i > 0:
            if i <=l and l< i+n[i]+1:
                l = i
                res.add(i)
            i-=1
        if l >= 0 and l < n[0] + 1:
            return True
        return False