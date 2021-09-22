# https://www.hackerearth.com/challenges/competitive/hackerearth-test-draft-3-115/problems/3370ea2a073948dbbcb1d82610c38d77/

def gen_para (n):
    # Write your code here
    ans = []
    def gen(i,j,res):
        if len(res) == 2*n:
            ans.append(res)
        else:
            if i > 0:
                gen(i-1,j,res+'(')
            if i<j and j > 0:
                gen(i,j-1,res+')')
    gen(n,n,'')
    return ans
    pass

n = int(input())

out_ = gen_para(n)
for i_out_ in out_:
    print (i_out_)