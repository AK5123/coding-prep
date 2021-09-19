def golden_char (key, st):
    # Write your code here
    d = set()
    for c in key:
        d.add(c)
    ans = 0
    for c in st:
        if c in d:
            ans += 1
    return ans
    pass

key = input()
str = input()

out_ = golden_char(key, str)
print (out_)