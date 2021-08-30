# https://leetcode.com/problems/kth-largest-element-in-an-array/
import random
class Solution:
    def findKthLargest(self, n, k):
        size = len(n)
        st = 0
        lt = size -1
        while st <= lt:
            j = st
            ran = random.randint(st,lt)
            n[ran],n[lt] = n[lt],n[ran]
            for i in range(st,lt):
                if n[i] <= n[lt]:
                    n[j],n[i] = n[i],n[j]
                    j += 1
            n[j],n[lt] = n[lt],n[j]
            if j == (size - k):
                return n[j]
            elif j > (size - k):
                lt = j - 1
            else:
                st = j + 1