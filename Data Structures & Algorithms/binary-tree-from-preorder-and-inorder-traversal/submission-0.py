# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        imap = {}
        for i, val in enumerate(inorder):
            imap[val] = i

        pre = 0

        def build(left, right):

            if left > right:
                return None
            nonlocal pre
            rootVal = preorder[pre]
            pre += 1


            root = TreeNode(rootVal)
            mid = imap[rootVal]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)

        