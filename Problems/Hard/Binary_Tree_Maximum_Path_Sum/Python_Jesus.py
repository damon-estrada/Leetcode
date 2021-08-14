# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # D&Q problem
        max_path_sum = [-sys.maxsize - 1]
        self.maxPath(root, max_path_sum)
        return max_path_sum[0]

    def maxPath(self, root, max_path_sum):
        if not root:
            return -sys.maxsize

        left = self.maxPath(root.left, max_path_sum)

        right = self.maxPath(root.right, max_path_sum)

        # These cases insure we inclue the middle case 
        # the only time that max will be just the left or just the righ node is if max is child node. This accounts for that 
        if root.val > max_path_sum[0]:
            max_path_sum[0] = root.val

        if root.val + left > max_path_sum[0]:
            max_path_sum[0] = root.val + left

        if root.val + right > max_path_sum[0]:
            max_path_sum[0] = root.val + right

        if root.val + left + right > max_path_sum[0]:
            max_path_sum[0] = root.val + left + right

        return max(root.val + left, root.val + right, root.val)