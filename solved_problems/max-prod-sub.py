# https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, a):
        res = a[0]
        cmin = a[0]
        cmax = a[0]
        for i in a[1:]:
            temp = cmax
            cmax = max(max(cmax*i,cmin*i),i)
            cmin = min(min(temp*i,cmin*i),i)
            if res < cmax:
                res = cmax
        return res        
       