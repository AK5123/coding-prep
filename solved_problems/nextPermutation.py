class Solution:
    def nextPermutation(self, n):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(n)-1,0,-1):
            if n[i-1] < n[i]:
                sm = i
                for j in range(i+1,len(n)):
                    if n[j] > n[i-1] and n[j] < n[sm]:
                        sm = j
                n[i-1],n[sm] = n[sm],n[i-1]
                temp = [k for k in n[i:]]
                temp.sort()
                for k in range(len(temp)):
                    n[i+k] = temp[k]
                return    
        n.reverse()       
        return       
    