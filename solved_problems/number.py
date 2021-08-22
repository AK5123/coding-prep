# https://www.hackerearth.com/challenges/competitive/hackerearth-test-draft-3-115/problems/e79093fbce804f90aeee90e9ff4d11cc/
def all_combos (string):
    # Write your code here
    def makes(cur,old):
        res = []
        for words in old:
            for char in cur:
                res.append(words+char)
        return res
    dic = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz',
    }
    res = ['']
    for char in string:
        res = makes(dic[char],res)
    return res
    pass

str = input()

out_ = all_combos(str)
for i_out_ in out_:
    print (i_out_)