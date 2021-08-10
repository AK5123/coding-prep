# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = 0
        while i < len(nums):
            if nums[i] == 0:
                nums[i],nums[k] = nums[k],nums[i]
                nums[j],nums[k] = nums[k],nums[j]
                j+=1
                k+=1
                i+=1
            elif nums[i] == 1:
                nums[i],nums[k] = nums[k],nums[i]
                k+=1
                i+=1
            elif nums[i] == 2:
                i+=1
        # print(nums,j,k)     