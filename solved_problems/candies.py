# https://www.hackerearth.com/challenges/competitive/hackerearth-test-draft-3-115/problems/c288d26a1c724b01be096c3ac6e919da/


def extra_candy (n, candies, extra_candies):
    # Write your code here
    big = max(candies)
    res = []
    for i in candies:
        if i+extra_candies >= big:
            res.append(1)
        else:
            res.append(0)
    return res
    pass

n = int(input())
candies = list(map(int, input().split()))
extra_candies = int(input())

out_ = extra_candy(n, candies, extra_candies)
print (' '.join(map(str, out_)))