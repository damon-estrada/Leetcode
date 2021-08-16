/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    int sumPath(TreeNode* root, int * stored) {
      if (root == NULL)
          return 0;
        
      int left = sumPath(root->left, stored);
      int right = sumPath(root->right, stored);
        
      int answer = max(left, right) + root->val;
      answer = max(answer, root->val);
      
        answer = max(answer, left + root->val + right);
        answer = max(*stored, answer);
      *stored = answer;
       return max(max(left, right) + root->val, root->val); 
        
        
    }
    
    int maxPathSum(TreeNode* root) {
        int answer = INT_MIN;
        sumPath(root, &answer);
        return answer;
    }
};