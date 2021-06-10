/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool hasPathSum(struct TreeNode* root, int targetSum){

        if (!root) // If the root is NULL, shouldn't be here return false
            return false;
        
        if (!root->left && !root->right && root->val == targetSum)
            // no children and value is equal to targetsum
            // found the path
            return true;
        
        return hasPathSum(root->left, targetSum - root->val) || hasPathSum(root->right, targetSum - root->val);
}