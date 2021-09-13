# String Anagrams (hard)
# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

s = "baa"
p = "aa"

d = {}
for c in p:
    d.setdefault(c,0)
    d[c] +=1

res = []
i = 0
matched = 0
for j in range(len(s)):
    if s[j] in d:
        d[s[j]] -= 1
        if d[s[j]] >= 0:
            matched += 1
    if j >= len(p):
        if s[i] in d:
            d[s[i]] += 1
            if d[s[i]] > 0:
                matched -= 1
        i += 1
    if matched == len(p):
        res.append(j-matched+1)




