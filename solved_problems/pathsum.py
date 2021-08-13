# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, su):
        def check(root,total):
            if root.left == None and root.right == None:
                return ( (total + root.val) == su)
            if root.left and root.right:
                return check(root.left,total+root.val) or check(root.right,total+root.val)
            else:
                if root.left:
                    return check(root.left,total+root.val)
                else:
                    return check(root.right,total+root.val)
        if not root:
            return False
        return check(root,0)     
           