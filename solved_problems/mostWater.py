# https://leetcode.com/problems/container-with-most-water
class Solution:
    def maxArea(self, h):
        a = 0
        l = 0
        r = len(h) - 1
        while l < r:
            a = max(a,min(h[l],h[r])*(r-l))
            if h[l] < h[r]:
                l+=1
            else:
                r-=1
        return a        
        