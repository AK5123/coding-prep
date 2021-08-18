# https://www.hackerearth.com/challenges/competitive/hackerearth-test-draft-3-115/problems/2554509ae41b46fd806eeb18e5aa996f/

def is_lexicographic (key, n, strings):
    # Write your code here
    dic = {}
    for i in range(len(key)):
        dic[key[i]] = i
    
    c =  []
    for st in strings:
        res = 0
        for i,char in enumerate(st):
            res += (dic[char]*(26**i))
        c.append(res)


    for t in range(len(strings)-1):
        if(c[t]<= c[t+1]):
            continue
        else:
            return 0
    return 1

    pass

key = input()
n = int(input())
str = []
for _ in range(n):
    str.append(input())

out_ = is_lexicographic(key, n, str)
print (out_)