# https://www.hackerearth.com/challenges/competitive/hackerearth-test-draft-3-115/problems/6a48c4d1bdae40818d2cbd8e66b23e12/
def merge(arr1,arr2, n1, n2):
    arr3 = []
    i=0
    j=0
    while i<n1 and j <n2:
        if arr1[i] < arr2[j]:
            i +=1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            arr3.append(arr1[i])
            i += 1
            j += 1
    return arr3


def array_intersection (n1, n2, n3, arr1, arr2, arr3):
    # Write your code here
    # arr1 = [[i,0] for i in arr1]
    # arr2 = [[i,0] for i in arr2]
    # arr3 = [[i,0] for i in arr3]

    arr4 = merge(arr1,arr2,n1,n2)
    arr5 = merge(arr4,arr3,len(arr4),n3)
    return arr5

    pass

n1 = int(input())
n2 = int(input())
n3 = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))

out_ = array_intersection(n1, n2, n3, arr1, arr2, arr3)
print (' '.join(map(str, out_)))