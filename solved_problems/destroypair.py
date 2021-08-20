#  https://www.hackerearth.com/challenges/competitive/hackerearth-test-draft-3-115/problems/3e79c7b1f92d49c9ac63cac81a01b6b6/
def remove_pair (a):
    # Write your code here
    i=0
    while i<(len(a)-1):
        if a[i] == a[i+1]:
            a = a[:i]+a[i+2:]
            if i != 0:
                i -= 1
        else:
            i += 1
    return a

    pass

string = input()

out_ = remove_pair(string)
print (out_)