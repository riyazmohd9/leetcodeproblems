# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        s = 0
        if root == None:
            return 0
        if root.left != None and root.left.left == None and root.left.right == None:
            s += root.left.val
        l = self.sumOfLeftLeaves(root.left)
        r = self.sumOfLeftLeaves(root.right)
        return l+r+s
        

        