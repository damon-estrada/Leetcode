# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

__author__ == "Yash Shah"


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # global variables retain values so, gotta clear them
        currentStack.clear() 
        Stack.clear()

        return inOrder(root, targetSum) #btw this makes use of pre-order traveral not in-order

        
currentStack = [] # making use of invariant that values in the currentStack are less than or equal to targetSum
Stack = [] # global stack to keep track of values that add up to targetSum
def inOrder(root, targetSum): 
    if (root == None):
        return Stack
    if(root.left == None and root.right == None): # leaf node
        currentStack.append(root.val) # appended to currentStack
        if (sum(currentStack) == targetSum): # if sum is equal to then that's the path
            Stack.append(currentStack.copy())
        currentStack.pop() # leaf node => so pop it right away
    else:
        currentStack.append(root.val) #first, this root, then left and then right
        inOrder(root.left, targetSum)
        inOrder(root.right, targetSum)
        currentStack.pop()        # pop it :)
        
    return Stack
