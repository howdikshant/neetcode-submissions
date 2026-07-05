# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        arr1 = []
        arr2 = []
        def findpath(node, target, arr):
            if not node:
                return 
            arr.append(node.val)

            if node.val == target:
                return
            if node.val > target:
                findpath(node.left, target, arr)
            else: 
                findpath(node.right, target, arr)

        findpath(root, p.val, arr1)
        findpath(root, q.val, arr2)
        res = 0
        n = len(arr1)
        m = len(arr2)
        y = min(n, m)
        for i in range(y):
            if arr1[i] == arr2[i]:
                res = arr1[i]
            
        return TreeNode(res)

            