# https://www.hackerearth.com/challenges/competitive/hackerearth-test-draft-3-115/problems/f788eeedf61444858d1607d83961988e/
def good_pairs (n, arr):
    # Write your code here
    d={}
    for c in arr:
        d.setdefault(c,0)
        d[c] += 1
    res = 0
    for i in d.values():
        if i > 1:
            res += (i*(i-1)/2)
    return int(res)
    pass

n = int(input())
arr = list(map(int, input().split()))

out_ = good_pairs(n, arr)
print (out_)