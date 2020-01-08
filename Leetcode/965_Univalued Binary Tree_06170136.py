# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        def travel(node, val):
            if not node:
                return True
            if node.val != val:
                return False
            return travel(node.left, val) and travel(node.right, val)
        
        return travel(root, root.val)
        
