# https://www.hackerearth.com/challenges/competitive/hackerearth-test-draft-3-115/problems/27fb489415914bd2896088486f767b74/
def missing_no (n, arr):
    # Write your code here
    total = n*(n+1)/2
    return int(total-sum(arr))
    pass

n = int(input())
arr = list(map(int, input().split()))

out_ = missing_no(n, arr)
print (out_)