# https://www.hackerearth.com/challenges/competitive/hackerearth-test-draft-3-115/problems/b95a3fdf76e6461f9d250477eb414186/

def sort_square (n, arr):
    # Write your code here
    res = []
    pos = len(arr)
    for i in range(len(arr)):
        if arr[i] >= 0:
            pos = i
            break
    neg = pos-1
    while neg >= 0 and pos < len(arr):
        if(abs(arr[neg]) < arr[pos]):
            res.append(arr[neg]**2)
            neg -= 1
        else:
            res.append(arr[pos]**2)
            pos += 1
    while neg >= 0:
        res.append(arr[neg]**2)
        neg -= 1
    while pos < len(arr):
        res.append(arr[pos]**2)
        pos += 1
    return res

    pass

n = int(input())
arr = list(map(int, input().split()))

out_ = sort_square(n, arr)
print (' '.join(map(str, out_)))