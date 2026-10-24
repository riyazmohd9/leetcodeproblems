# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        b = []
        
        def check(node, current_path, remaining_sum):
            if node is None:
                return
            
            # 1. Add current node to path
            current_path.append(node.val)
            
            # 2. Check if it's a leaf and the remaining sum matches the node's value
            if node.left is None and node.right is None:
                if remaining_sum == node.val:
                    b.append(current_path.copy())
            else:
                # 3. Recurse down children with the updated remaining sum
                check(node.left, current_path, remaining_sum - node.val)
                check(node.right, current_path, remaining_sum - node.val)
            
            # 4. Backtrack: remove the node before going back up
            current_path.pop()

        check(root, [], targetSum)
        return b
        