# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
class Solution:
    def generateParenthesis(self, n):
        res = []
        def gen(string,lb,rb):
            if lb == 0 and rb == 0:
                res.append(string)
                return
            else:
                if lb > 0:
                    gen(string+"(",lb-1,rb)
                if rb > 0 and rb > lb:
                    gen(string+")",lb,rb-1)
                return
        gen("",n,n)
        return res