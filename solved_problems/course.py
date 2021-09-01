# https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def findOrder(self, course, pre):
        
        def dfs(white,black,grey,arr,curr):
            grey.add(curr)
            for ele in range(len(arr)):
                if arr[curr][ele] == 1 and (ele not in black):
                    if (ele in grey):
                        return True
                    else:
                        ans = dfs(white,black,grey,arr,ele)
                        if ans:
                            return True
            grey.remove(curr)
            black.add(curr)
            return False                      
            
            
        def findc(arr):
            white = {a for a in range(len(arr))}
            black = set()
            grey = set()
            while len(black) != len(arr):
                curr = white.pop()
                grey.add(curr)
                ans = dfs(white,black,grey,arr,curr)
                if ans:
                    return True
            return False
        
        def topological(i,vis,result,arr):
            vis.add(i)
            for ele in range(len(arr)):
                if arr[i][ele] == 1 and (ele not in vis):
                    topological(ele,vis,result,arr)
            result.append(i)        
                    
        
        arr = []
        for i in range(course):
            arr.append([0]*course)
        for i in pre:
            arr[i[1]][i[0]] = 1
            
        if findc(arr):
            return []
        else:
            result = []
            vis = set()
            for i in range(course):
                if i not in vis:
                    topological(i,vis,result,arr)
            return result[::-1]        
                    