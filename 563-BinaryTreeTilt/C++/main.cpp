/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    int result = 0;
    
public:
    int helper(TreeNode* root) {        
        int left = 0, right = 0;
        if (root->left) {
            left = helper(root->left);
        }
        
        if (root->right) {
            right = helper(root->right);
        }
        
        result += abs(left - right);
        return left + right + root->val;
    }
    int findTilt(TreeNode* root) {
        if (!root) return 0;
        
        helper(root);
        return result;
    }
};