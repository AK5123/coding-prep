# Permutation in a String
# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
from copy import deepcopy
s = "eidbaooo"
pattern="ab"
pmap = {}
for c in pattern:
    pmap.setdefault(c, 0)
    pmap[c] += 1


def check(dic):
    for ele in dic:
        if dic[ele] != 0:
            return False
    return True

def find(s,dmap):
    i=0
    pmap = deepcopy(dmap)
    for j in range(len(s)):
        if s[j] in pmap:
            pmap[s[j]] -= 1
            while pmap[s[j]] < 0:
                pmap[s[i]] += 1
                i += 1
            rs = check(pmap)
            if rs:
                return True
        else:
            i = j+1
            pmap = deepcopy(dmap)
    return False

print(find(s,pmap))


        
