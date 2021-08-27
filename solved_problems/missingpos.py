def missing_pos (n, arr):
    # Write your code here
    i = 0
    for i in range(n):
        while(arr[i] != i+1 and arr[i] != '*'):
            pos = arr[i]-1
            if arr[i] > n or arr[i] <=0:
                arr[i] = '*'
            else:
                arr[i],arr[pos] = arr[pos],arr[i]
    for i in range(n):
        if arr[i] == '*':
            return i+1
    return n   

    pass

n = int(input())
arr = list(map(int, input().split()))

out_ = missing_pos(n, arr)
print (out_)