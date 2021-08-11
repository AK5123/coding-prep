# https://leetcode.com/problems/find-peak-element/
class Solution:
    def findPeakElement(self, nums):
        st,end = 0,len(nums)-1
        while st<end:
            mid = int((st+end)/2)
            if nums[mid] < nums[mid+1]:
                st = mid+1
            else:
                end = mid
        return st