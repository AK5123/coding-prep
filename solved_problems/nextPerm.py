
def next_permutation (n, arr):
    # Write your code here
    i = n - 1
    while(i>=0):
        if(i>0):
            if arr[i-1] >= arr[i]:
                i -= 1
            else:
                break
        else:
            break
    if i == 0:
        arr = arr[::-1]
        return arr
    else:
        tar = i-1
        ans = i
        for l in range(i+1,n):
            if arr[l]<= arr[ans] and arr[l] > arr[tar]:
                ans = l
        arr[tar],arr[ans] = arr[ans],arr[tar]
        x = arr[tar+1::]
        arr = arr[:tar+1]+x[::-1]

        return arr
        
    pass

n = int(input())
arr = list(map(int, input().split()))

out_ = next_permutation(n, arr)
print (' '.join(map(str, out_)))