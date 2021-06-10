/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    public boolean hasPathSum(TreeNode root, int targetSum) {
        
        boolean has_path_to_sum = false;
        
        if (root!=null){
           has_path_to_sum = recursivePathSum(root, targetSum);        
            }
        return has_path_to_sum;
    }
    
    private boolean recursivePathSum(TreeNode root, int targetSum) {
        boolean has_path_to_sum = false;
        int missing_sum = targetSum - root.val;

        //Base case 
        if (root.left == null && root.right == null && root.val == targetSum){
            has_path_to_sum = true;
        }

        //go left 
        else if (root.left != null){
            has_path_to_sum = recursivePathSum(root.left, missing_sum);
        }

        //go right 
        if (root.right != null && !has_path_to_sum){
             has_path_to_sum = recursivePathSum(root.right, missing_sum);                
        }
        return has_path_to_sum;
    }
}