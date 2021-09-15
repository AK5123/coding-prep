def two_sum (n, arr, target):
    # Write your code here
    res = 0
    d = {}
    for i in arr:
        if i in d:
            res += d[i]
        d.setdefault(target-i,0)
        d[target-i] += 1
    return res
    pass

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

out_ = two_sum(n, arr, target)
print (out_)