def perimeter (m, n, arr):
    # Write your code here
    def find(i,j,vis):
        vis[i][j] = 1
        res = 0
        sides = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
        for side in sides:
            if (side[0]>=0 and side[0]<m and side[1]>=0 and side[1]<n):
                if (arr[side[0]][side[1]] == 1 and  vis[side[0]][side[1]] == 0):
                    res += find(side[0],side[1],vis)
                else:
                    if( vis[side[0]][side[1]] == 0):
                        res += 1
            else:
                res += 1
        return res
        
    vis = []
    for i in range(m):
        vis.append([0]*n)
    for i in range(m):
        for j in range(n):
            if vis[i][j] == 0 and arr[i][j] == 1:
                res = find(i,j,vis)
                return res
    pass

m = int(input())
n = int(input())
arr = [list(map(int, input().split())) for i in range(m)]

out_ = perimeter(m, n, arr)
print (out_)