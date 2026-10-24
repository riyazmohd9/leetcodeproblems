# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        def solve(root,num):
            if root == None:
                return 0

            num = num*2 + root.val
            if root.left == None and root.right == None:
                return num
                
            return solve(root.left,num)+solve(root.right,num) 
        return solve(root,0)

        