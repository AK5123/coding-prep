class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        j = 0
        res = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while j < len(nums2):
            res.append(nums2[j])
            j+=1
        while i<len(nums1):
            res.append(nums1[i])
            i+=1
        s = int(len(res)/2)   
        if len(res)%2 == 0:
            return ((res[s]+res[s-1])/2.0)
        return res[s]/1.0