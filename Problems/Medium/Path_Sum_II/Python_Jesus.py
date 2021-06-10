# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        paths = []
        current_path = []
        if root != None:
            self.recursivePathSum(root, targetSum, current_path, paths)

        return paths

    # I dont want this to return anything i just want it dynamically keep
    # track off all the paths that lead to the target sum
    def recursivePathSum(self, root: TreeNode, targetSum: int, current_path: List[int], paths: List[int]):

        current_path.append(root.val)
        missing_sum = targetSum - root.val

        # Base case
        if root.left == None and root.right == None and root.val == targetSum:
            # Idk if there is a better way other than copying the array. In the
            # current implimentation you need to copy it or else you will miss
            # it up when you pop everything off
            paths.append(copy.deepcopy(current_path))

        # go left
        if root.left != None:
            self.recursivePathSum(root.left, missing_sum, current_path, paths)

        # go right
        if root.right != None:
            self.recursivePathSum(root.right, missing_sum, current_path, paths)
            # we need to pop since we are going back a layer in the recursion
        current_path.pop()
