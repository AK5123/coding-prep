# Given a string, find the length of the longest substring which has no repeating characters. 
tring="abbbb"
i = 0
j=0
dict = {}
res = 1
while i < len(tring):
    if tring[i] not in dict:
        dict[tring[i]] = 1
        res = max(res,len(dict))
    else:
        dict[tring[i]] += 1
        while dict[tring[i]] > 1:
            dict[tring[j]] -= 1
            if dict[tring[j]] == 0:
                del dict[tring[j]]
            j += 1
    i += 1

print(res)
