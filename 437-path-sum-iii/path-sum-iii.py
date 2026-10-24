# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        def check(root, l):
            if root is None:
                return 0
            
            l.append(root.val)
            count = 0
            temp = 0
            
            # Check for any valid sub-paths ending at the current node
            for i in reversed(l):
                temp += i
                if temp == targetSum:
                    count += 1
            
            # Recursively check left and right children and add up the counts
            count += check(root.left, l)
            count += check(root.right, l)
            
            # Backtrack
            l.pop()
            
            return count  # <--- Crucial fix: return the integer count!

        return check(root, [])

        