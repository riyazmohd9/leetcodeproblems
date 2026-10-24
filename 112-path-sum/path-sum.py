# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetsum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            return targetsum == root.val
        targetsum -= root.val
        l = self.hasPathSum(root.left,targetsum)
        r = self.hasPathSum(root.right,targetsum)
        return l or r

        