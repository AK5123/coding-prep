# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pat: str, s: str) -> bool:
        arr = s.split(" ")
        if len(arr) == len(pat):
            d = {}
            # s = {x for x in pat}
            for i,p in enumerate(pat):
                if p in d:
                    if d[p] != arr[i]:
                        return False
                else:
                    d[p] = arr[i]
            if len(set(d.values())) == len(d.keys()):
                return True
        return False    