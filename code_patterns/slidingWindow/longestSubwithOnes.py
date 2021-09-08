def longestOnes(nums, k):
    i=0
    ans=0
    zc = 0
    for j in range(len(nums)):
        if nums[j] == 0:
            zc += 1
        if zc > k:
            if nums[i] == 0:
                zc -= 1
            i += 1
        ans = max(ans,j-i+1)
            
    return ans
                   