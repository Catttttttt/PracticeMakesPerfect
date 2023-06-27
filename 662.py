# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 1
        arr = [[root, 1]]
        while arr:
            tmp = []
            for cur, i in arr:
                if cur.left:
                    tmp.append([cur.left, i*2])
                if cur.right:
                    tmp.append([cur.right, i*2+1])
            res = max(res, arr[-1][1]-arr[0][1]+1)
            arr = tmp
        return res
