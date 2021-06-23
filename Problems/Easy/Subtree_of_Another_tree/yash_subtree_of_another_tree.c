/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool compareNodes(struct TreeNode * first, struct TreeNode* second) 
{
    if (first == NULL && second == NULL)
        return true;
    else if (first != NULL && second != NULL) {
        if (first->val != second-> val)
            return false;
        else 
            return compareNodes(first->left, second->left) && compareNodes(first->right, second->right);
    }
    else
        return false;
}
bool newOne(struct TreeNode * root, struct TreeNode * subRoot) {
    if (!root)
        return false;
    if (root->val == subRoot-> val)
        return compareNodes(root, subRoot) || newOne(root->left, subRoot) || newOne(root->right, subRoot);
    
    return newOne(root->left, subRoot) || newOne(root->right, subRoot);
}

bool isSubtree(struct TreeNode* root, struct TreeNode* subRoot){
    return newOne(root, subRoot);
}

